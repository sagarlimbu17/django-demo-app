from django.forms import ModelForm, forms

from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean(self):
        clean_data = super().clean()
        if clean_data['weight'] > 100:
            raise forms.ValidationError("WEIGHT IS GREATER THAN 100")
        return clean_data
