import PySimpleGUI as sg
from controllers.main_controller import MainController

# Crear instancia del controlador principal
main_controller = MainController()

# Definir los diseños de las vistas principales
menu_layout = [
    [sg.Text("Menú principal", font=("Helvetica", 14), justification="center")],
    [sg.Button("Estudiantes", font=("Helvetica", 12), size=(20, 2))],
    [sg.Button("Materias", font=("Helvetica", 12), size=(20, 2))],
    [sg.Button("Salir", font=("Helvetica", 12), size=(20, 2))]
]

# Definir la ventana principal
window = sg.Window("Sistema de Gestión de Matrículas", menu_layout, size=(400, 300))

# Loop principal
while True:
    event, values = window.read()

    # Cerrar la aplicación si se hace clic en "Salir" o se cierra la ventana
    if event == "Salir" or event == sg.WIN_CLOSED:
        break

    # Abrir la vista de estudiantes si se hace clic en "Estudiantes"
    elif event == "Estudiantes":
        main_controller.show_student_menu()

    # Abrir la vista de materias si se hace clic en "Materias"
    elif event == "Materias":
        main_controller.show_subject_menu()

window.close()
