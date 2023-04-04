from models.subject import Subject
from subject_view.subject_Details_GUI import SubjectDetailsGUI


class SubjectController:
    def __init__(self):
        self.subjects = []

    def create(self, subject_data):
        subject = Subject(subject_data["code"], subject_data["name"])
        subject.save()
        self.subjects = self.get_all()

    def get_all(self):
        return Subject.all()

    def delete(self, subject):
        subject.delete()
        self.subjects = self.get_all()

    def update(self, subject, subject_data):
        subject.code = subject_data["code"]
        subject.name = subject_data["name"]
        subject.save()

    def edit(self, subject):
        details_gui = SubjectDetailsGUI()
        details_gui.subject_code.update(value=subject.code)
        details_gui.subject_name.update(value=subject.name)
        event, values = details_gui.read()
        if event == "Guardar cambios":
            self.update(subject, values)
