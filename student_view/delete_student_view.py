import PySimpleGUI as sg


class DeleteStudentView:
    def __init__(self):
        self.layout = [
            [sg.Text("Ingrese el ID del estudiante que desea eliminar:")],
            [sg.Input(key="student_id")],
            [sg.Button("Eliminar"), sg.Button("Cancelar")],
        ]

    def get_student_id(self, event, values):
        if event == "Eliminar":
            return values["student_id"]
        return None
