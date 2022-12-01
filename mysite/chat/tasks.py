import json
from celery import shared_task

@shared_task
def send_message(self, chat_obj, message):
    chat_obj.send(text_data=json.dumps({
        'message': message
    }))
    # return "Hello channel!"