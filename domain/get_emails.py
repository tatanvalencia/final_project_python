import imaplib
import email

def get_emails(user_name, password, imap_url='imap.gmail.com'):
    try:
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(user_name, password)
        mail.select("[Gmail]/Spam")
        result, data = mail.search(None, 'ALL')
        email_ids = data[0].split()
        emails = []
        for email_id in email_ids:
            result, msg_data = mail.fetch(email_id, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            emails.append(msg)
        return emails
    except Exception as error:
        print(f'Error al obtener los correos electrónicos: {error}')
        return []