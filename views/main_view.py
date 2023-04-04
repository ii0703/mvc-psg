import PySimpleGUI as sg


class MainView:
    def __init__(self):
        self.layout = [
            [sg.Text("Sistema de Matrícula")],
            [sg.Button("Estudiantes"), sg.Button("Materias"), sg.Button("Salir")],
        ]

    def get_event(self, event, values):
        return event
