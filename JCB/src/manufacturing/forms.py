from django import forms
from .models import Employeee,Testt,Parttt

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employeee
		fields = '__all__'

class TestForm(forms.ModelForm):
	class Meta:
		model = Testt
		fields = '__all__'


class partForm(forms.ModelForm):
	class Meta:
		model = Parttt
		fields = '__all__'