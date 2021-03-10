from os.path import basename
from typing import Union, List
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

SMTP_HOSTNAME = "localhost"
SMTP_PORT = 25


def send_email(
    user: str,
    password: str,
    from_address: str,
    to_address: Union[str, List[str]],
    subject: str,
    body: str,
    file_paths: List[str],
):
    mime_text = MIMEMultipart(body)
    mime_text.set_param("Subject", subject)
    mime_text.set_param("From", from_address)
    mime_text.set_param("To", to_address)
    mime_text.set_param("Date", formatdate())

    for file_path in file_paths:
        with open(file_path, "rb") as f:
            file_name = basename(file_path)
            mime_application = MIMEApplication(f.read(), Name=file_name)
            mime_application.set_param(
                "Content-Disposition", f"attachment; filename={file_name}"
            )
            mime_text.attach(mime_application)

    smtp = smtplib.SMTP(host=SMTP_HOSTNAME, port=SMTP_PORT)
    smtp.login(user=user, password=password)
    smtp.sendmail(
        from_addr=from_address, to_addrs=to_address, msg=mime_text.as_string()
    )
    smtp.close()
