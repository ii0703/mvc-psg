import PySimpleGUI as sg


class StudentGUI:
    def __init__(self, students=None):
        self.students = students or []
        self.layout = [
            [sg.Text("Estudiantes")],
            [sg.Listbox(values=[f"{student.id} - {student.name}" for student in self.students], size=(40, 10),
                        key="Estudiantes")],
            [sg.Button("Agregar estudiante")],
            [sg.Button("Ver detalles"), sg.Button("Eliminar"), sg.Button("Volver")]
        ]
        self.window = sg.Window("Estudiantes").Layout(self.layout)

    def read(self):
        return self.window.read()

    def hide(self):
        self.window.Hide()

    def un_hide(self):
        self.window.UnHide()
