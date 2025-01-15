from uuid import UUID


class TokenDataDTO:
    """"""

    def __init__(self, uid: UUID, iac: bool, isf: bool):
        self.uid = uid
        self.iac = iac
        self.isf = isf

    def dict(self):
        return {
            "uid": self.uid,
            "iac": self.iac,
            "isf": self.isf
        }