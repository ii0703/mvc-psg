import PySimpleGUI as sg


class EnrollmentDetailsGUI:
    def __init__(self, enrollment):
        self.enrollment = enrollment
        self.layout = [
            [sg.Text("ID del estudiante:"), sg.InputText(key="ID del estudiante", default_text=enrollment.student.id)],
            [sg.Text("Nombre del estudiante:"),
             sg.InputText(key="Nombre del estudiante", default_text=enrollment.student.name)],
            [sg.Text("Edad del estudiante:"),
             sg.InputText(key="Edad del estudiante", default_text=enrollment.student.age)],
            [sg.Text("Materia:"), sg.Text(enrollment.subject.name)],
            [sg.Button("Guardar cambios")]
        ]
        self.window = sg.Window("Detalles de la matrícula").Layout(self.layout)

    def read(self):
        return self.window.Read()
