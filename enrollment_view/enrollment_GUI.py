import PySimpleGUI as sg


class EnrollmentGUI:
    def __init__(self, enrollment_controller, student_controller, subject_controller):
        self.enrollment_controller = enrollment_controller
        self.student_controller = student_controller
        self.subject_controller = subject_controller

    def show(self):
        layout = [
            [sg.Text("Matrícula de Estudiantes en Materias", font=("Helvetica", 14), justification="center")],
            [sg.Text("Seleccione la Materia", font=("Helvetica", 12))],
            [sg.Listbox(values=self.subject_controller.get_all_subjects_names(), size=(30, 6), key="-SUBJECT LIST-", enable_events=True)],
            [sg.Text("Seleccione el Estudiante", font=("Helvetica", 12))],
            [sg.Listbox(values=self.student_controller.get_all_students_names(), size=(30, 6), key="-STUDENT LIST-", enable_events=True)],
            [sg.Button("Matricular", font=("Helvetica", 12), size=(10, 1), disabled=True, key="-ENROLL-"),
             sg.Button("Cancelar", font=("Helvetica", 12), size=(10, 1))]
        ]

        window = sg.Window("Matrícula de Estudiantes en Materias", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                break

            if event == "-SUBJECT LIST-":
                selected_subject = values["-SUBJECT LIST-"][0]
                students_registered = self.enrollment_controller.get_enrolled_students(selected_subject)
                students_names = self.student_controller.get_all_students_names()

                students_names_with_state = []
                for student_name in students_names:
                    if student_name in students_registered:
                        students_names_with_state.append(f"{student_name} (Matriculado)")
                    else:
                        students_names_with_state.append(student_name)

                window["-STUDENT LIST-"].update(values=students_names_with_state)
                window["-ENROLL-"].update(disabled=True)

            if event == "-STUDENT LIST-":
                selected_student = values["-STUDENT LIST-"]
                selected_subject = values["-SUBJECT LIST-"][0]

                if selected_student:
                    window["-ENROLL-"].update(disabled=False)

            if event == "-ENROLL-":
                selected_student = values["-STUDENT LIST-"][0]
                selected_subject = values["-SUBJECT LIST-"][0]

                enrollment_data = {"student_name": selected_student, "subject_code": selected_subject}
                self.enrollment_controller.create_enrollment(enrollment_data)

                sg.popup(f"El estudiante {selected_student} ha sido matriculado en la materia {selected_subject}.", title="Matrícula exitosa")

                window["-SUBJECT LIST-"].update(values=self.subject_controller.get_all_subjects_names())
                window["-STUDENT LIST-"].update(values=self.student_controller.get_all_students_names(), disabled=True)
                window["-ENROLL-"].update(disabled=True)

        window.close()
