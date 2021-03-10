import unittest

from src.smtp import send_email
from os.path import dirname

TEST_DATA_PATH = "src/testdata"


class TestSmtp(unittest.TestCase):
    def test_send_email(self):
        send_email(
            user="user1@mail.example.com",
            password="xxxxxxxx",
            from_address="user1@mail.example.com",
            to_address="user2@mail.example.com",
            subject="test subject",
            body="test body",
            file_paths=[f"{TEST_DATA_PATH}/textfile.txt"],
        )