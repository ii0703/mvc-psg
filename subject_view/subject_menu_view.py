import PySimpleGUI as sg

class SubjectMenuView:
    def __init__(self):
        # Definir el diseño de la ventana
        self.layout = [
            [sg.Text("Menú de Materias", font=("Helvetica", 14), justification="center")],
            [sg.Button("Registrar materia", font=("Helvetica", 12), size=(20, 2))],
            [sg.Button("Listar materias", font=("Helvetica", 12), size=(20, 2))],
            [sg.Button("Volver", font=("Helvetica", 12), size=(20, 2))]
        ]

    def show_menu(self):
        # Crear la ventana y mostrar el menú de materias
        window = sg.Window("Menú de Materias", self.layout, size=(400, 300))

        while True:
            event, values = window.read()

            # Cerrar la ventana si se hace clic en "Volver" o se cierra la ventana
            if event == "Volver" or event == sg.WIN_CLOSED:
                break

            # Llamar al método correspondiente en el controlador de materias si se hace clic en "Registrar materia" o "Listar materias"
            elif event == "Registrar materia":
                self.register_subject()

            elif event == "Listar materias":
                self.list_subjects()

        window.close()

    def register_subject(self):
        # Mostrar la vista de registro de materias
        pass

    def list_subjects(self):
        # Mostrar la vista de listado de materias
        pass
