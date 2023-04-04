import PySimpleGUI as sg


class CreateSubjectView:
    def __init__(self, subject_controller):
        self.subject_controller = subject_controller

    def show(self):
        # Definir el diseño de la ventana de creación de materias
        layout = [
            [sg.Text("Crear Materia", font=("Helvetica", 14), justification="center")],
            [sg.Text("Código:"), sg.Input(key="code")],
            [sg.Text("Nombre:"), sg.Input(key="name")],
            [sg.Button("Crear", font=("Helvetica", 12), size=(10, 1)), sg.Button("Cancelar", font=("Helvetica", 12), size=(10, 1))]
        ]

        # Crear la ventana de creación de materias
        window = sg.Window("Crear Materia", layout)

        while True:
            event, values = window.read()

            # Crear la materia al hacer clic en "Crear"
            if event == "Crear":
                code = values["code"]
                name = values["name"]
                if code and name:
                    self.subject_controller.create_subject(code, name)
                    sg.popup("Materia creada exitosamente")
                    break
                else:
                    sg.popup("Ingrese el código y el nombre de la materia")

            # Cerrar la ventana de creación de materias si se hace clic en "Cancelar" o se cierra la ventana
            elif event == "Cancelar" or event == sg.WIN_CLOSED:
                break

        window.close()
