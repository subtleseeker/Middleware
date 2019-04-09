from __future__ import absolute_import
from test_celery.celery import app
import time
from kombu import Queue

app.conf.task_default_queue = 'default'
app.conf.tasks_queues = (
    Queue('default', exchange ='default', routing_key='default'),
    Queue('add', exchange='add', routing_key='add'),
    Queue('multiply', exchange='multiply',routing_key='multiply'),
    Queue('prime',exchange='prime',routing_key='prime')
)

@app.task(queue='add')
def longtime_add(x, y):
    print('long time task begins')
    print ('long time task finished')
    return x + y

@app.task(queue='prime')
def return_prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True

@app.task(queue='multiply')
def multiply(x, y):
    return x*y
