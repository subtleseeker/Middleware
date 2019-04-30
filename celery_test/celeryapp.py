from __future__ import absolute_import
from celery import Celery




app = Celery('celery_test',
			broker = 'amqp://username:password@localhost/subtleseeker_vhost',
			backend= 'rpc://',
			include=['celery_test.tasks'])

# app = Celery('celery_test',
# 			broker = 'amqp://ruchin:ruchin123@172.26.42.183/ruchin__vhost',
#              backend='rpc://',
#              include=['celery_test.tasks'])
# app = Celery('celery_test',
#              broker='amqp://agam1:agam123@localhost/agam1_vhost',
#              backend='rpc://',
#              include=['celery_test.tasks'])
# app = Celery('celery_test',
#  			broker="amqp://bhanubb:bhanubhandari@localhost/bhanubhandari_vhost", 
#              backend='rpc://',
#              include=['celery_test.tasks'])


app.config_from_object('celery_test.celeryconfig')
