from models.normalized_job import NormalizedJob
from models.raw_job import RawJob
from utils.transform_utils import clean_title, clean_company

def transform_raw_job(raw: RawJob) -> NormalizedJob:
    clean_title(raw)
    clean_company(raw)