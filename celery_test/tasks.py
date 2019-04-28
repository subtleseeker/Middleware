# from __future__ import absolute_import
# from celery_test.celeryapp import app
# import time


# @app.task
# def longtime_add(x, y):
#     print('long time task begins')
#     # sleep 5 seconds
#     time.sleep(5)
#     print('long time task finished')
#     return x + y

# @app.task
# def longtime_multiply(x, y):
#     print('long time task begins')
#     # sleep 5 seconds
#     time.sleep(5)
#     print('long time task finished')
#     return x * y

from __future__ import absolute_import
from celery_test.celeryapp import app
import time
from kombu import Queue
import random

app.conf.task_default_queue = 'celery'
app.conf.tasks_queues = (
    Queue('noise', exchange ='celery', routing_key='noise'),
    Queue('add', exchange='celery', routing_key='add'),
    Queue('multiply', exchange='celery',routing_key='multiply'),
    Queue('brightness',exchange='celery',routing_key='brightness'),
    Queue('upgen',exchange='celery',routing_key='upgen')

)

# # @app.task(queue='add')
# # def longtime_add(x, y):
# #     print('long time task begins')
# #     print ('long time task finished')
# #     l = []
# #     for i in range(5):
# #         k = x[i]+y[i]
# #         print("(((" ,k)
# #         l.append(k)

# #     return l

@app.task(queue='add')
def longtime_add(x, y):
    print('long time task begins')
    print ('long time task finished')
    return x+y


# @app.task(queue='prime')
# def return_prime(x):
#     print('long time task begins')
#     for i in range(2, x-1):
#         if x % i == 0:
#             return False
#     else:
#         return True

@app.task(queue='multiply')
def longtime_multiply(x, y):
    print('long time task begins')
    print ('long time task finished')
    return x*y

# @app.task(queue='upgen')
# def upgenerator():
#     N = 3
#     M = 5
#     password = []
#     username = []
#     for x in range(N):
#         s1 = ""
#         s2 = ""
        
#         # print 10 random values
#         # between 1 and 100
#         for y in range(M):
#             s1 = s1 + chr(random.randint(97, 122))
#             z = random.randint(1,2)
#             if(z  == 1):
#                 s2 = s2 + chr(random.randint(97,122))
#             else:
#                 s2 = s2 + str(random.randint(1, 9))
#                 username.append(s1)
#                 password.append(s2)
#     return (username, password)



# ################## delete me ##################################
# # from __future__ import absolute_import
# # from test_celery.celery import app
# # import time
# # from kombu import Queue
# # import random

# # app.conf.task_default_queue = 'default'
# # app.conf.tasks_queues = (
# #     Queue('default', exchange ='default', routing_key='default'),
# #     Queue('add', exchange='add', routing_key='add'),
# #     Queue('multiply', exchange='multiply',routing_key='multiply'),
# #     Queue('prime',exchange='prime',routing_key='prime')
# # )

# # @app.task(queue='add')
# # def longtime_add(x, y):
# #     print('long time task begins')
# #     print ('long time task finished')
# #     return x + y

# # @app.task(queue='prime')
# # def return_prime(x):
# #     print('long time task begins')
# #     for i in range(2, x-1):
# #         if x % i == 0:
# #             return False
# #     else:
# #         return True

# # @app.task(queue='multiply')
# # def multiply(x, y):
# #     return x*y

# # @app.task()
# # def upgenerator():
# #     N = 3
# #     M = 5
# #     password = []
# #     username = []
# #     for x in range(N):
# #         s1 = ""
# #         s2 = ""
        
# #         # print 10 random values
# #         # between 1 and 100
# #         for y in range(M):
# #             s1 = s1 + chr(random.randint(97, 122))
# #             z = random.randint(1,2)
# #             if(z  == 1):
# #                 s2 = s2 + chr(random.randint(97,122))
# #             else:
# #                 s2 = s2 + str(random.randint(1, 9))
# #                 username.append(s1)
# #                 password.append(s2)
# #     return (username, password)
