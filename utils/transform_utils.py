import re
from datetime import datetime
from typing import Optional, Tuple, Dict

def clean_title(raw_tile:str) -> str:
    if not raw_title:
        return ""
    title = raw_title.strip()
    title = title.encode("ascii", "ignore").decode()

    fluff_patterns = [
        r"(?i)urgently hiring[!.,\s]*",
        r"(?i)apply now[!.,\s]*",
        r"(?i)hiring now[!.,\s]*",
        r"(?i)new[!.,\s]*",
        r"🔥",
        r"⭐",
    ]

    for pattern in fluff_patterns:
        title = re.sub(pattern, "", title)

    title = re.sub(r"\s+", " ", title)

    title = re.sub(r"\s+([,:;.!?])", r"\1", title)

    return title.strip()


raw_company = '     🔥🔥🔥 Hiring for Acme (Pty) Ltd.  ⭐⭐⭐      '


def clean_company(raw_company:str) -> str:
    if not raw_company:
        return ""

    company = raw_company.strip()
    company = company.encode("ascii", "ignore").decode()

    fluff_pattern = [
        r"(?i)hiring for[!.,\s]*",
        r"(?i)recruiting for[!.,\s]*",
        r"(?i)urgently hiring[!.,\s]*",
    ]

    for pattern in fluff_pattern:
        company = re.sub(pattern, "", company)

    company = re.sub(
        r"(?i)\b(\(?pty\)?\s*ltd\.?|\(?pty\)?|ltd\.?|inc\.?|llc\.?|cc\.?)\b",
        "",
        company
    )

    # Remove any leftover "(" or "(." or "(," at the end
    company = re.sub(r"\(\s*[^\w]*$", "", company)

    company = re.sub(r"\s+", " ", company)
    company = re.sub(r"\s+([,:;.!?])", r"\1", company)
    final = company.strip()

    return final

# clean_description(raw_description:str) -> str:
#
# normalize_location(raw_location:str) -> str:
#
# detect_remote_from_location(raw_location:str) -> bool:
#
# detect_remote_from_text(raw_description:str) -> :
#
# parse_posted_date(raw_posted:str | None) -> dateTime | None:
#
# parse_salary(raw_salary:str | None) -> tuple[int | None, int | None, str | None:
#
# extract_skills(raw_descriptions:str) -> dict:
#
# detect_language(raw_description:str) -> str:
# return "en"

print(clean_company(raw_company))