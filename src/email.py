from typing import List


class Email:
    def __init__(
        self,
        from_address: str,
        to_addresses: List[str],
        subject: str,
        body: str,
        file_paths: List[str],
    ):
        self.from_address = from_address
        self.to_addresses = to_addresses
        self.subject = subject
        self.body = body
        self.file_paths = file_paths
