from typing import TypedDict, Optional

class RawJob(TypedDict):
    '''Fields as scraped from the HTML document.'''
    source: str
    external_id: str
    title_raw: str
    company_raw: str
    location_raw: str
    description_raw: str
    posted_raw: str | None
    salary_raw: str | None
    url: str

class SalaryInfo(TypedDict):
    min: Optional[int]
    max: Optional[int]
    currency: str
    period: str
