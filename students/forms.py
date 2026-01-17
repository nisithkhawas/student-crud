from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age<18:
            raise forms.ValidationError("Age must be 18")
        return age