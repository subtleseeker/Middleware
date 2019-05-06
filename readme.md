# Middleware

# How to run the project
In one terminal run- "python initial.py" from the parent directory   
Open the flask server at localhost:5000   
In other terminal run the celery worker- `celery worker --app=celery_test.celeryapp:app -Q add` from the parent directory   



The basic flow of the code is as follows: 
1. The client interacts with a webpage for uploading tasks, which is connected to a Flask backend. This Flask backend can host any number of clients and can be connected to multiple servers which run our tasks (called workers) at a time.   

The client uploads a file with a task.    

2. Once a task is received by Flask, it automatically forwards it to a celery worker which runs remotely. These workers can be made to run for multiple tasks or for a single task.    

3. The celery worker executes the task and outputs the result in the output file, which is automatically downloaded on the client. Flask plays a large role in connecting the client and the worker which executes the task. Flask acts as the middleware in this case.    

Please feel free to reach out in case of any questions.    

Project link: https://drive.google.com/open?id=1c4rzyHGWzdY-R_NriJ05NnpUekv3vSEH   

Links:    
[1]: https://tests4geeks.com/python-celery-rabbitmq-tutorial/   
[2]: https://avilpage.com/2014/11/scaling-celery-sending-tasks-to-remote.html   
[3]: http://docs.celeryproject.org/   
[4]: https://www.rabbitmq.com/documentation.html   
[5]: http://flask.pocoo.org/docs/1.0/   
