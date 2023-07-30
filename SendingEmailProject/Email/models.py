from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.IntegerField(db_index=True)
    name = models.CharField(max_length=255, help_text='Enter Employee Name', db_index=True, null=True, blank=True)
    birthdate = models.DateField(help_text='Enter Employee Birthdate')
    work_anniversary_date = models.DateField(help_text='Enter Employee work anniversary date')
    email = models.EmailField(max_length=255, help_text='Enter email Id', db_index=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name
