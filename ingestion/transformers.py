from models.normalized_job import NormalizedJob
from models.raw_job import RawJob
from utils.transform_utils import clean_title, clean_company, normalize_location, detect_remote_from_location, \
    detect_remote_from_text, clean_description, parse_posted_date, parse_salary, extract_skills, detect_language


def transform_raw_job(raw: RawJob) -> NormalizedJob:
    salary = parse_salary(raw.get("salary_raw"))
    print("transformer is running.")
    return {
        "source": raw.get("source"),
        "external_id": raw.get("external_id"),
        "title": clean_title(raw.get("title_raw")),
        "company": clean_company(raw.get("company_raw")),
        "location": normalize_location(raw.get("location_raw")),
        "is_remote": (
                detect_remote_from_location(raw.get("location_raw")) or
                detect_remote_from_text(raw.get("description_raw"))
        ),
        "description": clean_description(raw.get("description_raw")),
        "url": raw.get("url"),
        "posted_at": parse_posted_date(raw.get("posted_raw")),
        "salary_min": salary["min"] if salary else None,
        "salary_max": salary["max"] if salary else None,
        "currency": salary["currency"] if salary else None,
        "language": detect_language(raw.get("description_raw")),
        "skills": extract_skills(raw.get("description_raw")),
    }
