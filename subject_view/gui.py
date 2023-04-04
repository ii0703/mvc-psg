import PySimpleGUI as sg

from subject_view.create_subject_view import CreateSubjectView
from subject_view.delete_subject_view import DeleteSubjectView
from subject_view.list_subjects_view import ListSubjectsView
from subject_view.update_subject_view import UpdateSubjectView


class SubjectGUI:
    def __init__(self, subject_controller):
        self.subject_controller = subject_controller

    def run(self):
        # Definir el diseño de la ventana principal
        layout = [
            [sg.Text("Menú de Materias", font=("Helvetica", 14), justification="center")],
            [sg.Button("Listar Materias", font=("Helvetica", 12), size=(20, 2))],
            [sg.Button("Crear Materia", font=("Helvetica", 12), size=(20, 2))],
            [sg.Button("Actualizar Materia", font=("Helvetica", 12), size=(20, 2))],
            [sg.Button("Eliminar Materia", font=("Helvetica", 12), size=(20, 2))],
            [sg.Button("Volver", font=("Helvetica", 12), size=(20, 2))]
        ]

        # Crear la ventana principal
        window = sg.Window("Menú de Materias", layout, size=(400, 400))

        while True:
            event, values = window.read()

            # Mostrar la vista de listado de materias al hacer clic en "Listar Materias"
            if event == "Listar Materias":
                subjects = self.subject_controller.get_all_subjects()
                ListSubjectsView(subjects).show()

            # Mostrar la vista de creación de materias al hacer clic en "Crear Materia"
            elif event == "Crear Materia":
                CreateSubjectView(self.subject_controller).show()

            # Mostrar la vista de actualización de materias al hacer clic en "Actualizar Materia"
            elif event == "Actualizar Materia":
                subject_id = sg.popup_get_text("Ingrese el código de la materia a actualizar")
                subject = self.subject_controller.get_subject_by_code(subject_id)
                if subject:
                    UpdateSubjectView(self.subject_controller, subject).show()
                else:
                    sg.popup("No se encontró la materia")

            # Mostrar la vista de eliminación de materias al hacer clic en "Eliminar Materia"
            elif event == "Eliminar Materia":
                subject_id = sg.popup_get_text("Ingrese el código de la materia a eliminar")
                subject = self.subject_controller.get_subject_by_code(subject_id)
                if subject:
                    DeleteSubjectView(self.subject_controller, subject).show()
                else:
                    sg.popup("No se encontró la materia")

            # Cerrar la ventana si se hace clic en "Volver" o se cierra la ventana
            elif event == "Volver" or event == sg.WIN_CLOSED:
                break

        window.close()
