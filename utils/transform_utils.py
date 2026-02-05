import re
from html import unescape
from datetime import datetime, timedelta
from models.raw_job import SalaryInfo
from utils.skills import SKILLS

def clean_title(raw_title:str) -> str | None:
    try:
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
        #remove punctuation end of string
        title = re.sub(r"[!.,;:/]+$", "", title)

        return title.strip()
    except Exception:
        return None

def clean_company(raw_company:str) -> str | None:
    try:
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
    except Exception:
        return None

def normalize_location(raw_location:str) -> str | None:
    try:
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
    except Exception:
        return None

def detect_remote_from_location(raw_location:str) -> bool | None:
    try:
        if not raw_location:
            return False
        location = raw_location.strip()
        location = location.encode("ascii", "ignore").decode()
        location = re.sub(r"\s+", " ", location)
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
    except Exception:
        return None

def detect_remote_from_text(raw_description:str) -> bool | None:
    try:
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
    except Exception:
        return None

def clean_description(raw_description:str) -> str | None:
    try:
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
    except Exception:
        return None

def parse_posted_date(raw_posted_date: str | None) -> datetime | None:
    try:
        if not raw_posted_date:
            return None

        post_date = raw_posted_date.strip()
        post_date = post_date.encode("ascii", "ignore").decode()
        post_date = re.sub(r"[!?]", "", post_date)
        post_date = re.sub(r"\s+", " ", post_date).strip()
        post_date = re.sub(r"\s*([/-])\s*", r"\1", post_date)
        # Remove everything except digits, letters, slashes, dashes, and spaces
        post_date = re.sub(r"[^0-9a-zA-Z/\-\s]", " ", post_date)

        # Relative dates
        relative_date = re.search(r"(\d+)\s*days?\s*ago",post_date)
        if relative_date:
            return datetime.today() - timedelta(days=int(relative_date.group(1)))

        if "yesterday" in post_date:
            return datetime.today() - timedelta(days=1)

        # Absolute dates with a year
        absolute_formats = [
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%d-%m-%y",
            "%d/%m/%y",
            "%Y-%m-%d",
            "%d %B %Y",
            "%d %b %Y",
            "%d %B, %Y",
            "%d %b, %Y",
            "%d %B %y",
            "%d %b %y",
            "%m/%y",
            "%m-%y",
            "%m/%Y",
            "%m-%Y",
        ]

        for pattern in absolute_formats:
            try:
                return datetime.strptime(post_date, pattern)
            except ValueError:
                pass

        # Absolute dates without a year
        post_date_with_year = f"{post_date} {datetime.today().year}"

        no_year_formats = [
            "%d %B %Y",
            "%d %b %Y",
            "%d-%m-%Y",
            "%d/%m/%Y",
        ]

        for pattern in no_year_formats:
            try:
                return datetime.strptime(post_date_with_year, pattern)
            except ValueError:
                pass

        return None
    except Exception:
        return None

def parse_salary(raw_salary: str | None) -> SalaryInfo | None:
    try:
        if not raw_salary:
            return None

        salary = raw_salary.lower()
        salary = salary.encode("ascii", "ignore").decode()
        salary = re.sub(r"\s+", " ", salary)
        salary = salary.replace(",", "")

        # Remove junk punctuation
        salary = re.sub(r"[!?]", "", salary)

        # 1. No-salary patterns
        no_salary_patterns = [
            "market related",
            "negotiable",
            "competitive",
            "doe",
            "not disclosed",
        ]
        if any(p in salary for p in no_salary_patterns):
            return None

        # 2. Detect period
        if "per annum" in salary or "per year" in salary or "pa" in salary:
            period = "year"
        else:
            period = "month"

        # 3. Convert k → 000
        salary = re.sub(r"(\d+)\s*k", lambda m: str(int(m.group(1)) * 1000), salary)
        # Convert "70 000" → "70000"
        salary = re.sub(r"(\d)\s+(\d{3})", r"\1\2", salary)
        # 4. Extract numbers
        numbers = re.findall(r"\d+", salary)
        numbers = [int(n) for n in numbers]

        if not numbers:
            return None

        # 5. Determine min/max
        if len(numbers) == 1:
            min_salary = max_salary = numbers[0]
        else:
            min_salary, max_salary = numbers[0], numbers[1]

        return {
            "min": min_salary,
            "max": max_salary,
            "currency": "ZAR",
            "period": period,
        }
    except Exception:
        return None

def extract_skills(raw_description: str | None) -> list[str]:
    try:
        if not raw_description:
            return []

        skills = raw_description.lower()
        skills = skills.encode("ascii", "ignore").decode()
        skills = re.sub(r"\s+", " ", skills)

        found = []

        for skill in SKILLS:
            if skill in skills:
                found.append(skill)

        return found

    except Exception:
        return []

def detect_language(raw_description:str) -> str | None:
    try:
        return "en"
    except Exception:
        return None