from __future__ import absolute_import
from celery import Celery

app = Celery('celery_test',
             broker='amqp://agam1:agam123@localhost/agam1_vhost',
             backend='rpc://',
             include=['celery_test.tasks'])