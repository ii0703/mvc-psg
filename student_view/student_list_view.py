import PySimpleGUI as sg

class StudentListView:
    def __init__(self, student_model, main_controller):
        self.student_model = student_model
        self.main_controller = main_controller

        # Definimos las columnas de la tabla
        self.headers = ["ID", "Nombre", "Edad"]

        # Creamos el layout de la ventana
        self.layout = [
            [sg.Text("Lista de Estudiantes", font=("Helvetica", 20))],
            [sg.Table(values=self.student_model.get_data(),
                      headings=self.headers,
                      auto_size_columns=True,
                      justification='center',
                      key='-TABLE-',
                      row_height=35)],
            [sg.Button("Agregar", key='-CREATE-'),
             sg.Button("Editar", key='-UPDATE-', disabled=True),
             sg.Button("Eliminar", key='-DELETE-', disabled=True),
             sg.Button("Actualizar", key='-REFRESH-')]
        ]

        # Creamos la ventana
        self.window = sg.Window("Estudiantes", self.layout, resizable=True, finalize=True)

        # Asociamos los callbacks a los eventos de la ventana
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == '-CREATE-':
                self.create_student()
            elif event == '-UPDATE-':
                self.update_student(values['-TABLE-'][0])
            elif event == '-DELETE-':
                self.delete_student(values['-TABLE-'][0])
            elif event == '-REFRESH-':
                self.refresh_table(values)

    def create_student(self):
        # Llamamos al controlador de Crear Estudiante
        self.main_controller.show_create_student()

    def update_student(self, student_id):
        # Llamamos al controlador de Actualizar Estudiante
        self.main_controller.show_update_student(student_id)

    def delete_student(self, student_id):
        # Llamamos al controlador de Eliminar Estudiante
        self.main_controller.show_delete_student(student_id)

    def refresh_table(self, values):
        # Actualizamos la tabla
        self.window['-TABLE-'].update(values=self.student_model.get_data())
        self.window['-UPDATE-'].update(disabled=True)
        self.window['-DELETE-'].update(disabled=True)
