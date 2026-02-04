from typing import TypedDict, Optional
from datetime import datetime

class NormalizedJob(TypedDict):
    source: str
    external_id: str
    title: str
    company: str
    location: str
    is_remote: bool
    description: str
    url: str
    posted_at: datetime | None
    salary_min: int | None
    salary_max: int | None
    currency: str | None
    language: str
    skills: dict

