class Student:
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"ID: {self.id} - Name: {self.name} - Age: {self.age}"
