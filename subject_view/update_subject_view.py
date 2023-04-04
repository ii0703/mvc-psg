import PySimpleGUI as sg


class UpdateSubjectView:
    def __init__(self, subject_controller):
        self.subject_controller = subject_controller

    def show(self):
        # Obtener la lista de materias y sus códigos
        subjects = self.subject_controller.get_subjects()
        subject_codes = [subject.code for subject in subjects]

        # Definir el diseño de la ventana de actualización de materias
        layout = [
            [sg.Text("Actualizar Materia", font=("Helvetica", 14), justification="center")],
            [sg.Text("Seleccione la materia a actualizar:")],
            [sg.Listbox(values=subject_codes, key="subject_code")],
            [sg.Text("Nuevo nombre:"), sg.InputText(key="subject_name")],
            [sg.Button("Actualizar", font=("Helvetica", 12), size=(10, 1)), sg.Button("Cancelar", font=("Helvetica", 12), size=(10, 1))]
        ]

        # Crear la ventana de actualización de materias
        window = sg.Window("Actualizar Materia", layout)

        while True:
            event, values = window.read()

            # Actualizar la materia seleccionada al hacer clic en "Actualizar"
            if event == "Actualizar":
                subject_code = values["subject_code"][0]
                subject_name = values["subject_name"]
                if subject_code:
                    if subject_name:
                        self.subject_controller.update_subject(subject_code, subject_name)
                        sg.popup("Materia actualizada exitosamente")
                        break
                    else:
                        sg.popup("Ingrese un nuevo nombre para la materia")
                else:
                    sg.popup("Seleccione una materia")

            # Cerrar la ventana de actualización de materias si se hace clic en "Cancelar" o se cierra la ventana
            elif event == "Cancelar" or event == sg.WIN_CLOSED:
                break

        window.close()
