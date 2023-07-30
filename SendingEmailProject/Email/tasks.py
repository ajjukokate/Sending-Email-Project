from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task
from datetime import date
from .models import Employee
from django.db.models import Q


@shared_task(bind=True)
def send_birthday_anniversary_email():
    today = date.today()
    employees = Employee.objects.filter(
        Q(birthdate__day=today.day, birthdate__month=today.month) |
        Q(work_anniversary_date__day=today.day, work_anniversary_date__month=today.month)
    )

    for employee in employees:
        subject = 'Happy Birthday!' if employee.birthdate == today else 'Happy Work Anniversary!'
        html_message = render_to_string('wishes.html', {'employee': employee})
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, 'ajju03.kokate@gmail.com', [employee.email], html_message=html_message)