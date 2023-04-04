class Subject:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def __str__(self):
        return f"Code: {self.code} - Name: {self.name}"
