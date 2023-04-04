import PySimpleGUI as sg

class ListSubjectsView:
    def __init__(self, subjects):
        # Definir el diseño de la ventana
        self.layout = [
            [sg.Text("Listado de Materias", font=("Helvetica", 14), justification="center")],
            [sg.Table(values=self.get_table_values(subjects), headings=["Código", "Nombre"], justification="center", auto_size_columns=False, col_widths=[10, 30])],
            [sg.Button("Volver", font=("Helvetica", 12), size=(20, 2))]
        ]

    def show(self):
        # Crear la ventana y mostrar la vista de listado de materias
        window = sg.Window("Listado de Materias", self.layout, size=(400, 300))

        while True:
            event, values = window.read()

            # Cerrar la ventana si se hace clic en "Volver" o se cierra la ventana
            if event == "Volver" or event == sg.WIN_CLOSED:
                break

        window.close()

    def get_table_values(self, subjects):
        # Obtener los datos de las materias en formato de tabla para mostrar en la vista
        return [[subject.code, subject.name] for subject in subjects]
