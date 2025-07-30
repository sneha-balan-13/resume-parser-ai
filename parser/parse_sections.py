import re

def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"\+?\d[\d -]{8,13}\d", text)
    return match[0] if match else None

def extract_skills(text, keywords=None):
    keywords = keywords or ['Python', 'SQL', 'Excel', 'Power BI', 'Tableau', 'Machine Learning']
    found = [skill for skill in keywords if skill.lower() in text.lower()]
    return found
