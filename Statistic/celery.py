import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Basketball_statistic.settings')


app = Celery('Basketball_statistic')
app.config_from_object('django.conf:settings', namespace='Celery')
app.autodiscover_tasks()

 
