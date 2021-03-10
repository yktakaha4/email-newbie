from src.email import Email
from imaplib import IMAP4
from email import message_from_string
from email.header import decode_header, make_header
from typing import List
from base64 import urlsafe_b64decode

IMAP_HOSTNAME = "localhost"
IMAP_PORT = 143

imap4 = IMAP4(host=IMAP_HOSTNAME, port=IMAP_PORT)


def receive_email(
    user: str,
    password: str,
):
    imap4.login(user=user, password=password)

    imap4.select()
    _, data = imap4.search(None, "ALL")

    emails: List[Email] = []

    for num in data[0].split():
        _, data = imap4.fetch(message_set=num, message_parts="(RFC822)")
        mail = message_from_string(data[0][1].decode("utf-8"))

        from_address = mail["From"]
        to_address = mail["To"]
        subject = str(make_header(decode_header(mail["Subject"])))
        body = ""

        for part in mail.walk():
            if part.get_content_maintype() == "multipart":
                continue

            filename = part.get_filename()

            if not filename:
                body = urlsafe_b64decode(part.get_payload().encode("ASCII")).decode(
                    "utf-8"
                )

        emails.append(
            Email(
                from_address=from_address,
                to_address=to_address,
                subject=subject,
                body=body,
                file_paths=[],
            )
        )

    imap4.close()

    return emails
