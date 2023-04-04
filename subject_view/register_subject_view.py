import PySimpleGUI as sg

class RegisterSubjectView:
    def __init__(self):
        # Definir el diseño de la ventana
        self.layout = [
            [sg.Text("Registrar materia", font=("Helvetica", 14), justification="center")],
            [sg.Text("Código: "), sg.Input(key="code")],
            [sg.Text("Nombre: "), sg.Input(key="name")],
            [sg.Button("Guardar", font=("Helvetica", 12), size=(20, 2))],
            [sg.Button("Cancelar", font=("Helvetica", 12), size=(20, 2))]
        ]

    def show(self):
        # Crear la ventana y mostrar la vista de registro de materias
        window = sg.Window("Registrar materia", self.layout, size=(400, 300))

        while True:
            event, values = window.read()

            # Cerrar la ventana si se hace clic en "Cancelar" o se cierra la ventana
            if event == "Cancelar" or event == sg.WIN_CLOSED:
                break

            # Llamar al método correspondiente en el controlador de materias si se hace clic en "Guardar"
            elif event == "Guardar":
                code = values["code"]
                name = values["name"]

                # Validar los campos antes de guardar la materia
                if code and name:
                    # Llamar al método para guardar la materia en el controlador de materias
                    pass

        window.close()
