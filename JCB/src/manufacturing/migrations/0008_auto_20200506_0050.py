# Generated by Django 3.0.5 on 2020-05-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0007_auto_20200506_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeee',
            name='emp_number',
            field=models.IntegerField(unique=True),
        ),
    ]
