from typing import TypedDict
from datetime import datetime

class NormalizedJob(TypedDict):
    source: str
    external_id: str
    title: str | None
    company: str | None
    location: str | None
    is_remote: bool
    description: str | None
    url: str
    posted_at: datetime | None
    salary_min: int | None
    salary_max: int | None
    currency: str | None
    language: str | None
    skills: list[str]

