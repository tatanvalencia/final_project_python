import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.get_emails import get_emails
from domain.classify_emails import classify_emails
from domain.generate_pdf import generate_pdf
from domain.train_model import train_model
from domain.extract_features import extract_features
from utils.constants import constants

if __name__ == "__main__":
    user_name = constants.USER_NAME
    password = constants.PASSWORD
    emails = get_emails(user_name, password)
    print(f'Se han recuperado {len(emails)} correos electrónicos.')
    model = train_model()
    phishing_emails = classify_emails(emails, model)
    if phishing_emails:
        print(f'Se han detectado {len(phishing_emails)} correos sospechosos de Phishing.')
        for email in phishing_emails:
            print(f'Correo sospechoso de Phishing detectado: {email['from']}')
        generate_pdf(phishing_emails)
    else:
        print('No se han detectado correos sospechosos de Phishing.')