from enrollment_view.enrollment_GUI import EnrollmentGUI
from enrollment_view.enrollment_details import EnrollmentDetailsGUI
from models.enrollment import Enrollment
from models.student import Student
from models.subject import Subject
from student_view.student_details import StudentDetailsGUI


class EnrollmentController:
    def __init__(self, enrollment_model: Enrollment, student_model: Student, subject_model: Subject,
                 student_details_view: StudentDetailsGUI, enrollment_view: EnrollmentGUI):
        self.enrollment_model = enrollment_model
        self.student_model = student_model
        self.subject_model = subject_model
        self.student_details_view = student_details_view
        self.enrollment_view = enrollment_view


    def create(self, students, subjects):
        details_gui = EnrollmentDetailsGUI(students, subjects)
        event, values = details_gui.read()
        if event == "Guardar cambios":
            student_id = values["ID del estudiante"]
            subject_code = values["Código de la materia"]
            enrollment = Enrollment(student_id, subject_code)
            self.enrollments.append(enrollment)
            self.gui.update_list(
                [f"{enrollment.student_id} - {enrollment.subject_code}" for enrollment in self.enrollments])
            return True
        return False

    def read(self):
        event, values = self.gui.read()
        if event == "Eliminar":
            index = values["Inscripciones"][0]
            del self.enrollments[index]
            self.gui.update_list(
                [f"{enrollment.student_id} - {enrollment.subject_code}" for enrollment in self.enrollments])
        return event, values
