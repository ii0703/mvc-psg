class Enrollment:
    def __init__(self, student_id: int, subject_code: str):
        self.student_id = student_id
        self.subject_code = subject_code

    def __str__(self):
        return f"Student ID: {self.student_id} - Subject Code: {self.subject_code}"
