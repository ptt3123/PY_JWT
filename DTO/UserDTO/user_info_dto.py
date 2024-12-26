class UserInfoDTO:
    """"""

    def __init__(self, username: str,first_name: str, last_name: str):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def dict(self):
        return {
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }