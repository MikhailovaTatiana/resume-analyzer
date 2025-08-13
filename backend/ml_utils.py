from typing import List
import re

def find_missing_keywords(resume_text: str, keywords: List[str]) -> List[str]:
    resume_lower = (resume_text or "").lower()
    tokens = set(re.findall(r'\b\w+\b', resume_lower))
    missing: List[str] = []
    for kw in keywords or []:
        kw_lower = kw.lower()
        if " " in kw_lower:
            # multi-word phrase: check substring presence
            if kw_lower not in resume_lower:
                missing.append(kw)
        else:
            # single word: check token presence
            if kw_lower not in tokens:
                missing.append(kw)
    return missing

def compute_keyword_coverage(resume_text: str, keywords: List[str]) -> float:
    """Return percentage of provided keywords found in the resume text.

    Coverage = (present_keywords / total_keywords) * 100
    """
    total = len(keywords or [])
    if total == 0:
        return 0.0
    missing = find_missing_keywords(resume_text, keywords)
    present = total - len(missing)
    return round((present / total) * 100.0, 2)
