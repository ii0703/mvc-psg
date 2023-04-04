from controllers.enrollment_controller import EnrollmentController
from controllers.student_controller import StudentController
from controllers.subject_controller import SubjectController
from enrollment_view.enrollment_GUI import EnrollmentGUI
from models.enrollment import Enrollment
from models.student import Student
from models.subject import Subject
from student_view.create_student_view import CreateStudentView
from student_view.delete_student_view import DeleteStudentView
from student_view.gui import StudentGUI
from student_view.student_details import StudentDetailsGUI
from student_view.student_list_view import StudentListView
from student_view.update_student_view import UpdateStudentView
from subject_view.create_subject_view import CreateSubjectView
from subject_view.delete_subject_view import DeleteSubjectView
from subject_view.gui import SubjectGUI
from subject_view.list_subjects_view import ListSubjectsView
from subject_view.subject_Details_GUI import SubjectDetailsGUI
from subject_view.update_subject_view import UpdateSubjectView
from views.main_view import MainView


class MainController:
    def __init__(self):
        # Se crean las instancias de los modelos
        self.student_model = Student(0,'',0)
        self.subject_model = Subject(0,'')
        self.enrollment_model = Enrollment(self.student_model, self.subject_model)

        # Se crean las instancias de las vistas
        self.student_list_view = StudentListView(self.student_model, self)
        self.create_student_view = CreateStudentView(self.student_model, self)
        self.update_student_view = UpdateStudentView(self.student_model, self)
        self.delete_student_view = DeleteStudentView(self.student_model, self)

        self.subject_list_view = ListSubjectsView(self.subject_model, self)
        self.create_subject_view = CreateSubjectView(self.subject_model, self)
        self.update_subject_view = UpdateSubjectView(self.subject_model, self)
        self.delete_subject_view = DeleteSubjectView(self.subject_model, self)

        self.student_details_view = StudentDetailsGUI()
        self.enrollment_view = EnrollmentGUI(self.enrollment_model, self.student_details_view)

        # Se crea la instancia del controlador principal de la aplicación
        self.main_view = MainView(self)

    def start(self):
        self.main_view.show()


    def run(self):
        while True:
            if not self.student_gui:
                self.student_controller.students = self.student_controller.get_all()
                self.student_gui = StudentGUI(self.student_controller.students)
            event, values = self.student_gui.read()
            if event == "Agregar estudiante":
                details_gui = StudentDetailsGUI()
                event, values = details_gui.read()
                if event == "Guardar cambios":
                    student = {"id": values["ID del estudiante"], "name": values["Nombre del estudiante"], "age": values["Edad del estudiante"]}
                    self.student_controller.create(student)
            elif event == "Eliminar":
                index = values["Estudiantes"][0]
                student = self.student_controller.students[index]
                self.student_controller.delete(student)
                self.student_controller.students = self.student_controller.get_all()
                self.student_gui.update_list([f"{student.id} - {student.name}" for student in self.student_controller.students])
            elif event == "Ver detalles":
                index = values["Estudiantes"][0]
                student = self.student_controller.students[index]
                self.enrollment_controller.enrollments = self.enrollment_controller.get_by_student(student.id)
                self.subject_controller.subjects = self.subject_controller.get_all()
                self.subject_gui = SubjectGUI(self.subject_controller.subjects)
                while True:
                    event, values = self.subject_gui.read()
                    if event == "Agregar materia":
                        details_gui = SubjectDetailsGUI()
                        event, values = details_gui.read()
                        if event == "Guardar cambios":
                            subject = {"code": values["Código de la materia"], "name": values["Nombre de la materia"]}
                            self.subject_controller.create(subject)
                    elif event == "Eliminar":
                        index = values["Materias"][0]
                        subject = self.subject_controller.subjects[index]
                        self.subject_controller.delete(subject)
                        self.subject_controller.subjects = self.subject_controller.get_all()
                        self.subject_gui.update_list([f"{subject.code} - {subject.name}" for subject in self.subject_controller.subjects])
                    elif event == "Ver detalles":
                        index = values["Materias"][0]
                        subject = self.subject_controller.subjects[index]
                        self.enrollment_controller.create(self.student_controller.students, self.subject_controller.subjects)
                        self.enrollment_controller.enrollments = self.enrollment_controller.get_by_subject(subject.code)
                        while True:
                            event, values = self.enrollment_controller.gui.read()
                            if event == "Eliminar":
                                self.enrollment_controller.read()
                            else:
                                break
                    else:
                        break
            else:
                break
