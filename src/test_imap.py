import unittest

from src.imap import receive_email
from os.path import dirname

TEST_DATA_PATH = "src/testdata"


class TestImap(unittest.TestCase):
    def test_receive_email(self):
        emails = receive_email(
            user="user2@mail.example.com",
            password="yyyyyyyy",
        )

        for email in emails:
            print(email.subject)
