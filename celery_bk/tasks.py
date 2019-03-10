from celery_bk.initial import app
# from celery.exceptions import Reject
import time

# The variable `acks_late=True` makes the system Fault Tolerant
@app.task(acks_late=True)
def longtime_mul(x, y):
    print("Long time multiplication task begins")
    time.sleep(5)
    z = x * y
    print("Long time multiplication task finished")
    return z

# @app.task
# def longtime_add(x,y):
#     print("long time task begins")
#     time.sleep(5)
#     print("Long time task finished")
#     return x+y


# @app.task
# def add(x, y):
#     return x + y

# Fault tolerance is implemented by the variable `acks_late=True`
# @app.task(acks_late=True)
# def longtime_div(x, y):
#     print("Long time division task begins")
#     try:
#         z = x / y
#         print("Long time division task finished")
#         return z
#     except ZeroDivisionError as exc:
#         raise Reject(exc, requeue=False)
