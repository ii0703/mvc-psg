import PySimpleGUI as sg

class CreateStudentView:
    def __init__(self, controller):
        self.controller = controller

    def get_layout(self):
        layout = [
            [sg.Text("Nombre"), sg.InputText(key="name")],
            [sg.Text("Edad"), sg.InputText(key="age")],
            [sg.Button("Crear"), sg.Button("Cancelar")]
        ]
        return layout

    def run(self):
        window = sg.Window("Crear Estudiante", self.get_layout())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break
            elif event == "Crear":
                name = values["name"]
                age = values["age"]
                self.controller.create_student(name, age)
                sg.popup("Estudiante creado con éxito.")
                window.close()
                break
        window.close()
