from django.db import models
from django.urls import reverse
from django.core.validators import (
									EmailValidator,
									MaxValueValidator,
									MinValueValidator,
									MaxLengthValidator,
									MinLengthValidator
									)




class Employeee(models.Model):
	
	GENDER=(
		('M','Male'),
		('F','Female'),
		('O','Others'),
		)

	Name=models.CharField(max_length=30)
	emp_number=models.IntegerField(unique=True)
	address=models.CharField(max_length=100)
	phone_number=models.CharField(max_length=15)
	email=models.CharField(max_length=50,validators=[EmailValidator("email address is not valid")])
	gender=models.CharField(max_length=1,choices=GENDER)
	age=models.IntegerField(null=True,validators=[
												    MaxValueValidator(62,message="Not a valid age"),
												    MinValueValidator(23,message="too young! Not a valid age")
												    ])
	designation=models.CharField(max_length=50)

	# this will show list objects by name in admin
	def __str__(self):
		return self.Name



	def get_absolute_url(self):
		return reverse("manufacturing:employee_update",kwargs={'id':self.id}) 


class Testt(models.Model):
	
	name=models.CharField(max_length=30)
	gstn=models.CharField(max_length=15)
	phone_number=models.CharField(max_length=10)
	bill=models.IntegerField()
	email=models.CharField(max_length=50,validators=[EmailValidator("email address is not valid")])
	description=models.TextField()
	date=models.DateField(auto_now=False, auto_now_add=False,help_text="Please use the following format: <em>YYYY-MM-DD</em>")

	sign=models.ForeignKey('Employeee',on_delete=models.CASCADE)

	# this will show list objects by name in admin
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("manufacturing:supview",kwargs={'id':self.id}) 


class Parttt(models.Model):

	TYPE=(
		('A','Chassis'),
		('B','Electrical'),
		('C','Engine'),
		('D','Transmission'),
		('E','Hydraulic'),
		('F','Others'),
		)
	
	name=models.CharField(max_length=30)
	serial_no=models.CharField(max_length=15,unique=True)
	typ=models.CharField(max_length=1,choices=TYPE)
	description=models.TextField()
	workers=models.ManyToManyField('Employeee')
	status=models.BooleanField()
	# this will show list objects by name in admin
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("manufacturing:partview",kwargs={'id':self.id}) 