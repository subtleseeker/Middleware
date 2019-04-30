from test_celery.celery import app
import time

import requests
import pandas as pd
import numpy as np
import random  

# from worker import app

# The variable `acks_late=True` makes the system Fault Tolerant
# Any functions that has to be run as background tasks need to be decorated with the celery.task decorator


@app.task(acks_late=True)
def longtime_add(x,y):
    print("long time task begins")
    time.sleep(5)
    print("Long time task finished")
    return x+y

@app.task(acks_late=True)
def username_password_generator(N):
    # N = int(input())
    # M = int(input())
    N = 2
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

    # return password
    return (username, password)

@app.task(acks_late=True)
def matrix_multiplication():
    print("Yeyeye")

@app.task(acks_late=True)
def multiplication():
    print("Do it yourself..")



# @app.task(bind=True, name='fetch_bitcoin_price_index')
# def fetch_bitcoin_price_index(self, start_date, end_date):
#     url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start='+start_date+'&end='+end_date
#     response = requests.get(url)
#     if not response.ok:
#         raise ValueError('Unexpected status code:' + response.status_code)
#     return [{'date': key, 'value': value} for key, value in response.json()['bpi'].items()]


# @app.task(bind=True, name='calculate_moving_average')
# def calculate_moving_average(self, args, window):
#     df = pd.DataFrame(args)
#     df['ma'] = df['value'].rolling(window=window, center=False).mean()
#     return list(df.replace(np.nan, '', regex=True).T.to_dict().values())
