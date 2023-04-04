import PySimpleGUI as sg


class EnrollmentView:
    def __init__(self, student_controller, subject_controller, enrollment_controller):
        self.student_controller = student_controller
        self.subject_controller = subject_controller
        self.enrollment_controller = enrollment_controller

    def show(self):
        # Obtener la lista de estudiantes y materias
        students = self.student_controller.get_students()
        student_names = [student.name for student in students]
        subjects = self.subject_controller.get_subjects()
        subject_names = [subject.name for subject in subjects]

        # Definir el diseño de la ventana de matrícula
        layout = [
            [sg.Text("Matrícula de Estudiantes en Materias", font=("Helvetica", 14), justification="center")],
            [sg.Text("Estudiante:"), sg.Listbox(values=student_names, key="student_name", size=(30, 5)), sg.Text("Materia:"), sg.Listbox(values=subject_names, key="subject_name", size=(30, 5))],
            [sg.Button("Agregar", font=("Helvetica", 12), size=(10, 1)), sg.Button("Cancelar", font=("Helvetica", 12), size=(10, 1))]
        ]

        # Crear la ventana de matrícula
        window = sg.Window("Matrícula", layout)

        while True:
            event, values = window.read()

            # Agregar la matrícula al hacer clic en "Agregar"
            if event == "Agregar":
                student_name = values["student_name"][0]
                subject_name = values["subject_name"][0]
                if student_name and subject_name:
                    student = self.student_controller.get_student_by_name(student_name)
                    subject = self.subject_controller.get_subject_by_name(subject_name)
                    self.enrollment_controller.add_enrollment(student.id, subject.code)
                    sg.popup("Estudiante matriculado exitosamente")
                    break
                else:
                    sg.popup("Seleccione un estudiante y una materia")

            # Cerrar la ventana de matrícula si se hace clic en "Cancelar" o se cierra la ventana
            elif event == "Cancelar" or event == sg.WIN_CLOSED:
                break

        window.close()


# import PySimpleGUI as sg
#
#
# class EnrollmentListGUI:
#     def __init__(self, enrollments):
#         self.enrollments = enrollments
#         self.layout = [
#             [sg.Listbox([enrollment.student.name for enrollment in enrollments], size=(20, 6), key="Estudiantes"),
#              sg.Button("Ver detalles"), sg.Button("Eliminar")]
#         ]
#         self.window = sg.Window("Estudiantes matriculados").Layout(self.layout)
#
#     def read(self):
#         return self.window.Read()
