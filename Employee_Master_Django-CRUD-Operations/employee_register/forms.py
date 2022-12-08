from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_code','fullname','mobile_number','designation')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code',
            'mobile_number':'Mobile Number',
            'designation':'Designation'
        }
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['designation'].empty_label='Select'
        self.fields['emp_code'].required = False