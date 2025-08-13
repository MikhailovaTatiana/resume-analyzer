from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io
import pytesseract
from ml_utils import find_missing_keywords, compute_keyword_coverage
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    keywords: str | None = Form(None),
    job_description: str | None = Form(None),
):
    try:
        file_bytes = await file.read()
    except Exception as exc:
        logging.exception("Failed to read uploaded file")
        raise HTTPException(status_code=400, detail=f"Failed to read uploaded file: {exc}")

    text = ""

    try:
        if file.filename.lower().endswith(".pdf"):
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if not page_text or page_text.strip() == "":
                        image = page.to_image(resolution=300).original
                        ocr_text = pytesseract.image_to_string(image)
                        text += (ocr_text or "") + "\n"
                    else:
                        text += page_text + "\n"
        else:
            text = file_bytes.decode("utf-8", errors="ignore")
    except Exception as exc:
        logging.exception("Failed to extract text from file")
        raise HTTPException(status_code=400, detail=f"Failed to extract text: {exc}")

    text = (text or "").strip()
    if not text:
        raise HTTPException(status_code=422, detail="No text could be extracted from the uploaded file")

    logging.info(f"Extracted text (first 1000 chars): {repr(text[:1000])}")

    provided_keywords = keywords if (keywords and keywords.strip()) else job_description
    if not provided_keywords or not provided_keywords.strip():
        raise HTTPException(status_code=422, detail="Either 'keywords' or 'job_description' must be provided")

    keyword_list = [k.strip() for k in (provided_keywords or "").split(",") if k.strip()]
    if not keyword_list:
        raise HTTPException(status_code=422, detail="At least one keyword must be provided")

    score = compute_keyword_coverage(text, keyword_list)
    missing = find_missing_keywords(text, keyword_list)

    return {"score": score, "missing_keywords": missing}


@app.get("/")
async def root():
    return {"message": "Keyword matcher API running"}
