from __future__ import absolute_import
from celery import Celery

# app = Celery('test_celery', 
# 			broker="amqp://bhanubb:bhanubhandari@localhost/bhanubhandari_vhost", 
# 			backend="rpc://", 
# 			include=['test_celery.tasks'])


# app = Celery('test_celery',
# 			broker = 'amqp://username:password@localhost/subtleseeker_vhost',
# 			backend= 'rpc://',
# 			include=['test_celery.tasks'])

# app = Celery('test_celery',
# 			broker = 'amqp://agam1:agam123@172.26.42.99/agam1_vhost',
# 			backend= 'rpc://',
# 			include=['test_celery.tasks'])

app = Celery('test_celery',
			broker = 'amqp://ruchin:ruchin123@172.26.42.183/ruchin__vhost',
			backend= 'rpc://',
			include=['test_celery.tasks'])

app.config_from_object('test_celery.celeryconfig')
