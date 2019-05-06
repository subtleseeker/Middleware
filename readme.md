# Middleware

## Installation

### Celery and RabbitMQ 
For celery and RabbitMQ, please refer to the link 1 for installation procedures related to Celery and RabbitMQ. 
In order for successful execution of the code on your machine, please change the configuration in celeryconfig.py to the configuration you create in RabbitMQ. Otherwise, connections will not be established. 

## How to run the project 
### Client Side 
In one terminal: 
1. Run- ```python initial.py``` from the parent directory.   
2. Open the flask server at localhost:5000. 
3. Create the file which you want to execute as a ".txt" file. 
4. Select the task and upload the file. 

### Celery 
1. In another terminal run the celery worker- `celery worker --app=celery_test.celeryapp:app -Q add` from the parent directory. (i.e. ```celery_test```)  



## Flow of the code 

The basic flow of the code is as follows: 
1. The client interacts with a webpage for uploading tasks, which is connected to a Flask backend. This Flask backend can host any number of clients and can be connected to multiple servers which run our tasks (called workers) at a time.   

The client uploads a file with a task.    

2. Once a task is received by Flask, it automatically forwards it to a celery worker which runs remotely. These workers can be made to run for multiple tasks or for a single task.    

3. The celery worker executes the task and outputs the result in the output file, which is automatically downloaded on the client. Flask plays a large role in connecting the client and the worker which executes the task. Flask acts as the middleware in this case.    

Please feel free to reach out in case of any questions.    

## Demonstration Video: Fault Tolerance and Load Balancing 
1. Video 1 (Load Balancing) and Video 2 (Worker: Failure and Recovery): https://drive.google.com/drive/folders/14wI51kcO9MGOCTzZuUb0bHy-L9cotulz
2. Video 3 (Worker: Works even when the other worker fails in Video 2): https://drive.google.com/drive/u/0/folders/122315BBZhdVSnV83Oq7AD6u4-5t2DreK  

## Code and reference links 
Project link: https://drive.google.com/open?id=1c4rzyHGWzdY-R_NriJ05NnpUekv3vSEH   

Links:    
[1]: https://tests4geeks.com/python-celery-rabbitmq-tutorial/   
[2]: https://avilpage.com/2014/11/scaling-celery-sending-tasks-to-remote.html   
[3]: http://docs.celeryproject.org/   
[4]: https://www.rabbitmq.com/documentation.html   
[5]: http://flask.pocoo.org/docs/1.0/   
