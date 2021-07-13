from django import forms
from testapp.models import Student

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()


class StudentForm1(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
