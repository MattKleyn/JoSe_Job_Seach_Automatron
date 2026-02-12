import re


def get_location(soup):
    details_list = soup.select(".detailsList")
    if not details_list:
        return None
    details = details_list[0]
    location_li = details.select_one("li")
    if not location_li:
        return None
    location_text = location_li.get_text(separator=" ", strip=True)
    return location_text


def get_salary(soup):
    details_list = soup.select(".detailsList")
    if not details_list:
        return None
    details = details_list[0]
    salary_li = details.find("li", class_="elipses")
    if not salary_li:
        return None
    salary_text = salary_li.get_text(" ", strip=True)
    return salary_text


def get_ext_id(soup):
    details_list = soup.select(".detailsList")
    if not details_list:
        return None
    details = details_list[0]
    ref_li = details.select(" li")[4].getText()
    if not ref_li:
        return None
    external_id = re.sub(r"(?i)reference:", "", ref_li)
    return external_id


def get_description1(soup):
    description = soup.select_one(".v-descrip")
    if not description:
        return None
    paragraphs = description.find_all("p")
    if not paragraphs:
        return None
    description_text = "\n".join(
        p.get_text(" ", strip=True) for p in paragraphs
    )
    return description_text


def get_description2(soup):
    description = soup.select_one(".c24-vacancy-details")
    if not description:
        return None
    paragraphs = description.find_all("p")
    if not paragraphs:
        return None
    description_text = "\n".join(
        p.get_text(" ", strip=True) for p in paragraphs
    )
    return description_text


FIELD_SELECTORS = {
    "external_id": [get_ext_id],
    "title": [lambda soup: soup.find("h1").contents[2].getText()],
    "company": [lambda soup: soup.find("strong").getText()],
    "location": [get_location],
    "description": [get_description1, get_description2],
    "salary": [get_salary],
}


def extract_with_fallback(soup, selectors):
    for selector in selectors:
        try:
            field = selector(soup)
            if field:
                print(f"[Scraper] {selector.__name__ if hasattr(selector, '__name__') else selector} succeeded")
                return field
        except Exception as e:
            print(f"[Scraper] {selector} failed: {e}")
            continue
    print("[Scraper] All selectors failed.")
    return None

