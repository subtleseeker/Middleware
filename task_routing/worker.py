import os
from celery import Celery


CELERY_BROKER_URL = 'amqp://bhanu:bhandari@broker:5672'


app = Celery(__name__)
app.conf.update({
    'broker_url': 'amqp://bhanu:bhandari@broker:5672',
    'imports': (
        'tasks',
    ),
    'task_routes': ('task_router.TaskRouter'),
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})
