from models.normalized_job import NormalizedJob
from models.raw_job import RawJob
from utils.transform_utils import clean_title, clean_company, normalize_location, detect_remote_from_location, \
    detect_remote_from_text, clean_description, parse_posted_date, parse_salary, extract_skills, detect_language


def transform_raw_job(raw: RawJob) -> NormalizedJob:
    clean_title(raw)
    clean_company(raw)
    normalize_location(raw)
    detect_remote_from_location(raw)
    detect_remote_from_text(raw)
    clean_description(raw)
    parse_posted_date(raw)
    parse_salary(raw)
    extract_skills(raw)
    detect_language(raw)
