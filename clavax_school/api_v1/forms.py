from django import forms

# Models Import
from .models import StudentClass, Student


class StudentClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = ('__all__')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ('first_name', 'last_name',)
        fields = ('__all__')
