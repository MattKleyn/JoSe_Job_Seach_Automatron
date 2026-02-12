CATEGORY_KEYWORDS = {
    "frontend": ["frontend", "front end", "react", "javascript", "ui", "ux", "ux/ui", "webflow"],
    "backend": ["backend", "back end", "python", "django", "flask", "api"],
    "fullstack": ["fullstack", "full stack"],
    "data": ["data analyst", "data engineer"],
    # "devops": ["devops", "cloud", "infrastructure"],
    # "mobile": ["android", "ios", "flutter", "react native"],
}


def detect_category(title: str | None) -> str | None:
    if not title:
        return None

    t = title.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(k in t for k in keywords):
            return category

    return None