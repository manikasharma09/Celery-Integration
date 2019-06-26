from celery import task 
from celery import shared_task 
# We can have either registered task or shared task
@task(name='summary') 
def send_import_summary():
     # code 
# or 
@shared_task 
def send_notifiction():
     print('hello')
     # code
