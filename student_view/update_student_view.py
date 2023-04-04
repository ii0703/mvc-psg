import PySimpleGUI as sg

class UpdateStudentView:
    def __init__(self, controller, student_id):
        self.controller = controller
        self.student_id = student_id

    def get_layout(self):
        student = self.controller.get_student(self.student_id)
        layout = [
            [sg.Text("Nombre"), sg.InputText(key="name", default_text=student.name)],
            [sg.Text("Edad"), sg.InputText(key="age", default_text=student.age)],
            [sg.Button("Actualizar"), sg.Button("Cancelar")]
        ]
        return layout

    def run(self):
        window = sg.Window("Actualizar Estudiante", self.get_layout())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break
            elif event == "Actualizar":
                name = values["name"]
                age = values["age"]
                self.controller.update_student(self.student_id, name, age)
                sg.popup("Estudiante actualizado con éxito.")
                window.close()
                break
        window.close()
