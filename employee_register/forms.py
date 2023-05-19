from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("fullname", "mobile", "emp_code", "position")
        labels = {"fullname": "Full Name", "emp_code": "EMP Code"}

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields["fullname"].widget.attrs["placeholder"] = "Enter your full name"
        self.fields["mobile"].widget.attrs["placeholder"] = "Your mobile number"
        self.fields["emp_code"].widget.attrs["placeholder"] = "Your employee code"
        self.fields["position"].empty_label = "Select"
