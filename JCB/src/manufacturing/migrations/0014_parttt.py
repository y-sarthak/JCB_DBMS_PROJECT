# Generated by Django 3.0.5 on 2020-05-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0013_auto_20200506_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parttt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('serial_no', models.CharField(max_length=15, unique=True)),
                ('typ', models.CharField(choices=[('A', 'Chassie'), ('B', 'Electrical'), ('C', 'Engine'), ('D', 'Transmission'), ('E', 'Hydraulic'), ('F', 'Others')], max_length=1)),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('workers', models.ManyToManyField(to='manufacturing.Employeee')),
            ],
        ),
    ]
