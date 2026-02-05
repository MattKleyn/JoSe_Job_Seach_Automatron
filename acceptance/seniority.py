def detect_seniority(title: str | None, description: str | None) -> str:
    text = f"{title or ''} {description or ''}".lower()

    if any(w in text for w in ["senior", "lead", "principal", "architect"]):
        return "senior"

    if any(w in text for w in ["intermediate", "mid-level", "mid level"]):
        return "mid"

    if any(w in text for w in ["junior", "entry level", "graduate"]):
        return "junior"

    return "unknown"