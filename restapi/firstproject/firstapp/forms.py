from django import forms
from firstapp.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal=self.cleaned_data['esal']
        if inputsal<5000:
            raise forms.ValidationError('the min sal should be 5000')
        return inputsal
    class Meta:
        model=Employee
        fields='__all__'