import PySimpleGUI as sg


class StudentDetailsGUI:
    def __init__(self, student=None):
        self.student = student or {"id": "", "name": "", "age": ""}
        self.layout = [
            [sg.Text("ID del estudiante"), sg.InputText(self.student["id"], key="ID del estudiante")],
            [sg.Text("Nombre del estudiante"), sg.InputText(self.student["name"], key="Nombre del estudiante")],
            [sg.Text("Edad del estudiante"), sg.InputText(self.student["age"], key="Edad del estudiante")],
            [sg.Button("Guardar cambios"), sg.Button("Cancelar")]
        ]
        self.window = sg.Window("Detalles del estudiante").Layout(self.layout)

    def read(self):
        return self.window.read()
