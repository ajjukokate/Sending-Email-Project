from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SendingEmailProject.settings')

app = Celery('SendingEmailProject')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#Celery Beat Task

CELERY_BEAT_SCHEDULE = {
    'send_birthday_anniversary_emails': {
        'task': 'Email.tasks.send_birthday_anniversary_email',
        'schedule': timedelta(days=1),
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')