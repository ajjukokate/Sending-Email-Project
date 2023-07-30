# Generated by Django 4.2.3 on 2023-07-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(db_index=True)),
                ('name', models.CharField(blank=True, db_index=True, help_text='Enter Employee Name', max_length=255, null=True)),
                ('birthdate', models.DateField(help_text='Enter Employee Birthdate')),
                ('work_anniversary_date', models.DateField(help_text='Enter Employee work anniversary date')),
                ('email', models.EmailField(db_index=True, help_text='Enter email Id', max_length=255)),
                ('type', models.CharField(choices=[('birthday', 'Birthday'), ('work_anniversary', 'Work Anniversary')], db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]