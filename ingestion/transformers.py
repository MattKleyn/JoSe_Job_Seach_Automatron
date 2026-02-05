from models.normalized_job import NormalizedJob
from models.raw_job import RawJob
from utils.transform_utils import clean_title, clean_company, normalize_location, detect_remote_from_location, \
    detect_remote_from_text, clean_description, parse_posted_date, parse_salary, extract_skills, detect_language


def transform_raw_job(raw: RawJob) -> NormalizedJob:
    salary = parse_salary(raw.get("salary"))

    return {
        "source": raw.get("source"),
        "external_id": raw.get("external_id"),
        "title": clean_title(raw.get("title")),
        "company": clean_company(raw.get("company")),
        "location": normalize_location(raw.get("location")),
        "is_remote": (
                detect_remote_from_location(raw.get("location")) or
                detect_remote_from_text(raw.get("description"))
        ),
        "description": clean_description(raw.get("description")),
        "url": raw.get("url"),
        "posted_at": parse_posted_date(raw.get("posted_at")),
        "salary_min": salary["min"] if salary else None,
        "salary_max": salary["max"] if salary else None,
        "currency": salary["currency"] if salary else None,
        "language": detect_language(raw.get("language")),
        "skills": extract_skills(raw.get("description")),
    }
