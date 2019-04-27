# Middleware
clsr is a client-server implemented in *go* with one master and different slaves using tcp. For understanding, please take a look at https://confusedcoders.com/general-programming/go-lang/create-a-basic-distributed-system-in-go-lang-part-1 \

# How to run the project
In one terminal run- "python initial.py" from the parent directory
Open the flask server at localhost:5000
In other terminal run the celery worker- "celery worker --app=celery_test.celeryapp:app -Q add" from the parent directory


