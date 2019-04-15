from __future__ import absolute_import
from celery import Celery

app = Celery('agam_test_celery',
             broker='amqp://agam1:agam123@localhost/agam1_vhost',
             backend='rpc://',
             include=['agam_test_celery.tasks'])