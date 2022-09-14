from Statistic.celery import app

from .service import Send_email

@app.task
def send_email_task(user_email):
    Send_email(user_email)