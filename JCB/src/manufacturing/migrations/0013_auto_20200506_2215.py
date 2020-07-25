# Generated by Django 3.0.5 on 2020-05-06 16:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0012_auto_20200506_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gstn', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=10)),
                ('bill', models.IntegerField()),
                ('email', models.CharField(max_length=50, validators=[django.core.validators.EmailValidator('email address is not valid')])),
                ('description', models.TextField()),
                ('date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>')),
                ('sign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Employeee')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
