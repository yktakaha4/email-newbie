import unittest

from src.email import Email
from src.smtp import send_email
from os.path import dirname

TEST_DATA_PATH = "src/testdata"


class TestSmtp(unittest.TestCase):
    def test_send_email(self):
        send_email(
            user="user1@mail.example.com",
            password="xxxxxxxx",
            emails=[
                Email(
                    from_address="user1@mail.example.com",
                    to_addresses=["user4@mail.example.com", "user5@mail.example.com"],
                    subject="test subject サブジェクト",
                    body="test body\nボディ",
                    file_paths=[f"{TEST_DATA_PATH}/textfile.txt"],
                )
            ],
        )
