import PySimpleGUI as sg


class DeleteSubjectView:
    def __init__(self, subject_controller):
        self.subject_controller = subject_controller

    def show(self):
        # Obtener la lista de materias y sus códigos
        subjects = self.subject_controller.get_subjects()
        subject_codes = [subject.code for subject in subjects]

        # Definir el diseño de la ventana de eliminación de materias
        layout = [
            [sg.Text("Eliminar Materia", font=("Helvetica", 14), justification="center")],
            [sg.Text("Seleccione la materia a eliminar:")],
            [sg.Listbox(values=subject_codes, key="subject_code")],
            [sg.Button("Eliminar", font=("Helvetica", 12), size=(10, 1)), sg.Button("Cancelar", font=("Helvetica", 12), size=(10, 1))]
        ]

        # Crear la ventana de eliminación de materias
        window = sg.Window("Eliminar Materia", layout)

        while True:
            event, values = window.read()

            # Eliminar la materia seleccionada al hacer clic en "Eliminar"
            if event == "Eliminar":
                subject_code = values["subject_code"][0]
                if subject_code:
                    self.subject_controller.delete_subject(subject_code)
                    sg.popup("Materia eliminada exitosamente")
                    break
                else:
                    sg.popup("Seleccione una materia")

            # Cerrar la ventana de eliminación de materias si se hace clic en "Cancelar" o se cierra la ventana
            elif event == "Cancelar" or event == sg.WIN_CLOSED:
                break

        window.close()
