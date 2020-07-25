# Generated by Django 3.0.5 on 2020-05-05 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0006_employee_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('emp_number', models.IntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(7, message='Employee Number should be of 7 digits'), django.core.validators.MinLengthValidator(7, message='Employee Number should be of 7 digits')])),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50, validators=[django.core.validators.EmailValidator('email address is not valid')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('age', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(62, message='Not a valid age'), django.core.validators.MinValueValidator(23, message='too young! Not a valid age')])),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
