from agam_test_celery.celery import app
from celery.result import AsyncResult
res = AsyncResult("b39b5a64-7eea-410e-b498-47ad21529265")
print(res.ready())