from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'standard', 'marks')


class AltStudentForm(StudentForm):
    def save_student(self):
        self.save()
