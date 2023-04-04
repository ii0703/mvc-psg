from models.student import Student
from student_view.student_details import StudentDetailsGUI


class StudentController:
    def __init__(self):
        self.students = []

    def create(self, student_data):
        student = Student(student_data["id"], student_data["name"], student_data["age"])
        student.save()
        self.students = self.get_all()

    def get_all(self):
        return Student.all()

    def delete(self, student):
        student.delete()
        self.students = self.get_all()

    def update(self, student, student_data):
        student.id = student_data["id"]
        student.name = student_data["name"]
        student.age = student_data["age"]
        student.save()

    def edit(self, student):
        details_gui = StudentDetailsGUI()
        details_gui.student_id.update(value=student.id)
        details_gui.student_name.update(value=student.name)
        details_gui.student_age.update(value=student.age)
        event, values = details_gui.read()
        if event == "Guardar cambios":
            self.update(student, values)
