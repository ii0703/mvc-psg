import PySimpleGUI as sg


class SubjectDetailsGUI:
    def __init__(self, subject_controller):
        self.subject_controller = subject_controller

    def show(self, subject):
        layout = [
            [sg.Text("Detalles de la Materia", font=("Helvetica", 14), justification="center")],
            [sg.Text(f"Código: {subject.code}")],
            [sg.Text(f"Nombre: {subject.name}")],
            [sg.Text(f"Créditos: {subject.credits}")],
            [sg.Text(f"Profesor: {subject.teacher}")],
            [sg.Button("Cerrar", font=("Helvetica", 12), size=(10, 1))]
        ]

        window = sg.Window("Detalles de la Materia", layout)

        while True:
            event, values = window.read()

            if event == "Cerrar" or event == sg.WIN_CLOSED:
                break

        window.close()
