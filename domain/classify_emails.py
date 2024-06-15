from domain.extract_features import extract_features

def classify_emails(emails, model):
    phishing_emails = []
    for email in emails:
        features = extract_features(email)
        prediction = model.predict([features["subject"]])
        if prediction[0] == "Phishing":
            phishing_emails.append(features)
    return phishing_emails