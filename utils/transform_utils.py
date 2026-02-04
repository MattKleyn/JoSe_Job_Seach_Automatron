import re
from html import unescape
from datetime import datetime
from typing import Optional, Tuple, Dict

def clean_title(raw_title:str) -> str:
    if not raw_title:
        return ""
    #remove whitespace beginning and end
    title = raw_title.strip()
    #remove emojis or non ascii characters
    title = title.encode("ascii", "ignore").decode()

    fluff_patterns = [
        r"(?i)urgently hiring[!.,\s]*",
        r"(?i)apply now[!.,\s]*",
        r"(?i)hiring now[!.,\s]*",
        r"(?i)new[!.,\s]*",
        r"🔥",
        r"⭐",
    ]
    #remove the fluff
    for pattern in fluff_patterns:
        title = re.sub(pattern, "", title)
    #remove excessive spaces
    title = re.sub(r"\s+", " ", title)
    #remove spaces around punctuation
    title = re.sub(r"\s+([,:;.!?])", r"\1", title)
    #remove punctuation
    title = re.sub(r"[!.,;:/]+$", "", title)

    return title.strip()

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
    company = re.sub(r"[!.,;:/]+$", "", company)
    final = company.strip()

    return final

def normalize_location(raw_location:str) -> str:
    if not raw_location:
        return ""

    location = raw_location.strip()
    location = location.encode("ascii", "ignore").decode()
    location = re.sub(r"\s+", " ", location)
    location = re.sub(r"\s+([,:;.!/])", r'\1', location)
    location = re.sub(r"[!.,;:/]+$", "", location)
    parts = [p.strip() for p in location.split(",") if p.strip()]
    if parts:
        return parts[0]

    return location.strip()

def detect_remote_from_location(raw_location:str) -> bool:
    if not raw_location:
        return False
    location = raw_location.strip()
    location = location.encode("ascii", "ignore").decode()
    location = re.sub(r"\s+", " ", location)
    print(location)
    remote_patterns = [
        r"(?i)\bremote\b",
        r"(?i)\bwork from home\b",
        r"(?i)\bwfh\b",
        r"(?i)\bhybrid\b",
        r"(?i)\banywhere\b",
    ]

    for pattern in remote_patterns:
        if re.search(pattern, location):
            return True

    return False

def detect_remote_from_text(raw_description:str) -> bool:
    if not raw_description:
        return False

    text = raw_description.strip()
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"\s+", " ", text)

    remote_patterns = [
        r"(?i)\bremote\b",
        r"(?i)\bfully remote\b",
        r"(?i)\b100% remote\b",
        r"(?i)\bwork from home\b",
        r"(?i)\bwfh\b",
        r"(?i)\bwork[-\s]?from[-\s]?anywhere\b",
        r"(?i)\bdistributed team\b",
        r"(?i)\bhybrid\b",
        r"(?i)\bflexible location\b",
    ]

    for pattern in remote_patterns:
        if re.search(pattern, text):
            return True

    return False

def clean_description(raw_description:str) -> str:
    if not raw_description:
        return ""

    text = raw_description.strip()

    # Decode HTML entities (&nbsp;, &amp;, etc.)
    text = unescape(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    text = text.encode("ascii", "ignore").decode()

    # Replace bullet characters with a dash
    text = re.sub(r"[•●▪■]", "-", text)

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[!.,;:/]+$", "", text)

    return text.strip()

# parse_posted_date(raw_posted:str | None) -> dateTime | None:
#
# parse_salary(raw_salary:str | None) -> tuple[int | None, int | None, str | None:
#
# extract_skills(raw_descriptions:str) -> dict:
#
def detect_language(raw_description:str) -> str:
    return "en"


