from os.path import basename
from typing import Union, List
import smtplib
from src.email import Email
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from typing import List

SMTP_HOSTNAME = "localhost"
SMTP_PORT = 25

smtp = smtplib.SMTP(host=SMTP_HOSTNAME, port=SMTP_PORT)


def send_email(user: str, password: str, emails: List[Email]):
    smtp.login(user=user, password=password)

    for email in emails:
        mime_multipart = MIMEMultipart()
        mime_multipart["Subject"] = email.subject
        mime_multipart["From"] = email.from_address
        mime_multipart["To"] = email.to_address
        mime_multipart["Date"] = formatdate()
        mime_multipart.attach(MIMEText(email.body))

        for file_path in email.file_paths:
            with open(file_path, "rb") as f:
                file_name = basename(file_path)
                mime_application = MIMEApplication(f.read(), Name=file_name)
                mime_application.set_param(
                    "Content-Disposition", f"attachment; filename={file_name}"
                )
                mime_multipart.attach(mime_application)

        smtp.sendmail(
            from_addr=email.from_address,
            to_addrs=email.to_address,
            msg=mime_multipart.as_string(),
        )

    smtp.close()
