import re

from email.header import decode_header
from email.utils import parsedate_tz

def extract_features(email):
    features = {}
    subject, encoding = decode_header(email["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")
    features["subject"] = subject
    from_ = email.get("From")
    features["from"] = from_
    date_tuple = parsedate_tz(email.get("Date"))
    if date_tuple:
        features["date"] = date_tuple
    if email.is_multipart():
        for part in email.walk():
            if part.get_content_type() == "text/plain":
                content = part.get_payload(decode=True).decode(errors='replace')
                break
    else:
        content = email.get_payload(decode=True).decode(errors='replace')
    features["content"] = content
    urls = re.findall(r'(https?://\S+)', content)
    features["urls"] = urls
    return features