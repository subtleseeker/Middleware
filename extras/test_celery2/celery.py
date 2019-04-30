from celery import Celery, bootsteps
from kombu import Exchange, Queue
import os

default_queue_name = 'default'
default_exchange_name = 'default'
default_routing_key = 'default'
deadletter_suffix = 'deadletter'
deadletter_queue_name = default_queue_name + '.{deadletter_suffix}'
deadletter_exchange_name = default_exchange_name + '.{deadletter_suffix}'
deadletter_routing_key = default_routing_key + '.{deadletter_suffix}'


class DeclareDLXnDLQ(bootsteps.StartStopStep):
    """c
    Celery Bootstep to declare the DL exchange and queues before the worker starts
        processing tasks
    """
    requires = {'celery.worker.components:Pool'}

    def start(self, worker):
        app = worker.app

        # Declare DLX and DLQ
        dlx = Exchange(deadletter_exchange_name, type='direct')

        dead_letter_queue = Queue(
            deadletter_queue_name, dlx, routing_key=deadletter_routing_key)

        with worker.app.pool.acquire() as conn:
            dead_letter_queue.bind(conn).declare()

app = Celery('test_celery',
			broker = 'amqp://subtleseeker:password@localhost/subtleseeker_vhost',
			backend= 'rpc://',
			include=['test_celery.tasks'])

            # broker='amqp://guest@localhost:5672//',

# app.conf.update({
#     # 'broker_url': 'amqp://bhanu:bhandari@broker:5672',
#     # 'imports': (
#     #     'tasks',
#     # ),
#     'task_routes': ('task_router.TaskRouter'),
#     'task_serializer': 'json',
#     'result_serializer': 'json',
#     'accept_content': ['json']})
	
# CELERY_BROKER_URL = 'amqp://bhanu:bhandari@broker:5672'
# CELERY_BROKER_URL = 'amqp://subtleseeker:password@localhost/subtleseeker_vhost'


# app = Celery(__name__)
# app.conf.update({
#     'broker_url': 'amqp://subtleseeker:password@localhost/subtleseeker_vhost',
#     # 'imports': (
#     #     'tasks',
#     # ),
#     # 'task_routes': ('task_router.TaskRouter'),
#     # 'task_serializer': 'json',
#     # 'result_serializer': 'json',
#     # 'accept_content': ['json']
#     })


default_exchange = Exchange(default_exchange_name, type='direct')
default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key,
    queue_arguments={
        'x-dead-letter-exchange': deadletter_exchange_name,
        'x-dead-letter-routing-key': deadletter_routing_key
    }
)

app.conf.task_queues = (default_queue, )

# Add steps to workers that declare DLX and DLQ if they don't exist
app.steps['worker'].add(DeclareDLXnDLQ)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key


