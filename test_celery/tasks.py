from test_celery.celery import app
import time

@app.task(acks_late=True)
def longtime_add(x,y):
    print("long time task begins")
    time.sleep(5)
    print("Long time task finished")
    return x+y