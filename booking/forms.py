from django import forms
from .models import Guest, Employee, Stay

# v class Guest v
class GuestCreateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')
class GuestUpdateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')

# v class Employee v
class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first', 'last', 'empid')
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first', 'last', 'empid')

# v class Stay v
class StayCreateForm(forms.ModelForm):
    class Mata:
        model = Stay
        fields = ('roomid','guestid','empid')