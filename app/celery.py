from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_redis.settings') 

app = Celery('django_celery_redis')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
