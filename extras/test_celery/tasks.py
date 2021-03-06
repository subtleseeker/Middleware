from __future__ import absolute_import
from test_celery.celery import app
import time
from kombu import Queue
import random

app.conf.task_default_queue = 'celery'
app.conf.tasks_queues = (
    Queue('default', exchange ='celery', routing_key='default'),
    Queue('add', exchange='celery', routing_key='add'),
    Queue('multiply', exchange='celery',routing_key='multiply'),
    Queue('prime',exchange='celery',routing_key='prime'),
    Queue('upgen',exchange='celery',routing_key='upgen')

)

# @app.task(queue='add')
# def longtime_add(x, y):
#     print('long time task begins')
#     print ('long time task finished')
#     l = []
#     for i in range(5):
#         k = x[i]+y[i]
#         print("(((" ,k)
#         l.append(k)

#     return l

@app.task(queue='add')
def longtime_add(x, y):
    try:
        print('long time task begins')
        print ('long time task finished')
        return x+y
    except ConnectionError as exc:
        self.retry(exc=exc,countdown=5)

@app.task(queue='prime')
def return_prime(x):
    try:
        print('long time task begins')
        for i in range(2, x-1):
            if x % i == 0:
                return False
        else:
            return True

    except ConnectionError as exc:
        self.retry(exc=exc,countdown=180)    
@app.task(queue='multiply')
def multiply(x, y):
    try: 
        return x*y
    except ConnectionError as exc:
        self.retry(exc=exc,countdown=180)
@app.task(queue='upgen')
def upgenerator():
    try:
        N = 3
        M = 5
        password = []
        username = []
        for x in range(N):
            s1 = ""
            s2 = ""
            
            # print 10 random values
            # between 1 and 100
            for y in range(M):
                s1 = s1 + chr(random.randint(97, 122))
                z = random.randint(1,2)
                if(z  == 1):
                    s2 = s2 + chr(random.randint(97,122))
                else:
                    s2 = s2 + str(random.randint(1, 9))
                    username.append(s1)
                    password.append(s2)
        return (username, password)

    except ConnectionError as exc:
        self.retry(exc=exc,countdown=180)    

################## delete me ##################################
# from _future_ import absolute_import
# from test_celery.celery import app
# import time
# from kombu import Queue
# import random

# app.conf.task_default_queue = 'default'
# app.conf.tasks_queues = (
#     Queue('default', exchange ='default', routing_key='default'),
#     Queue('add', exchange='add', routing_key='add'),
#     Queue('multiply', exchange='multiply',routing_key='multiply'),
#     Queue('prime',exchange='prime',routing_key='prime')
# )

# @app.task(queue='add')
# def longtime_add(x, y):
#     print('long time task begins')
#     print ('long time task finished')
#     return x + y

# @app.task(queue='prime')
# def return_prime(x):
#     print('long time task begins')
#     for i in range(2, x-1):
#         if x % i == 0:
#             return False
#     else:
#         return True

# @app.task(queue='multiply')
# def multiply(x, y):
#     return x*y

# @app.task()
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