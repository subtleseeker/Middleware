from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery', broker="amqp://bhanubb:bhanubhandari@localhost/bhanubhandari_vhost", backend="rpc://", include=['test_celery.tasks'])


