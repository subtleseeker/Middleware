# Middleware

## Installation

### Installing Celery and RabbitMQ  
To run the project, first install RabbitMQ and celery.   
1. Install celery using pip:      
```$ pip install celery``` 
2. Install RabbitMQ using apt:   
```$ sudo apt-get install rabbitmq-server```
3. Add `sbin` in path in `.bashrc`:   
```PATH=$PATH:/usr/local/sbin```   
4. Check if RabbitMQ is installed by: 
```$ rabbitmq-server```   
It should print:   
```Starting broker... completed with 10 plugins.```   
If it says 0 plugins, troubleshoot to install RabbitMQ properly.   
5. Configure RabbitMQ for celery:   
(if your username is jimmy)   
```
# add user 'jimmy' with password 'jimmy123'
$ rabbitmqctl add_user jimmy jimmy123
# add virtual host 'jimmy_vhost'
$ rabbitmqctl add_vhost jimmy_vhost
# add user tag 'jimmy_tag' for user 'jimmy'
$ rabbitmqctl set_user_tags jimmy jimmy_tag
# set permission for user 'jimmy' on virtual host 'jimmy_vhost'
$ rabbitmqctl set_permissions -p jimmy_vhost jimmy ".*" ".*" ".*"
```
6. Update the file celery_test/celeryapp.py according to your configuration as set in the previous step.   

## How to run the project 

After successfully installing RabbitMQ and celery, run the project on 2 or more terminals as follows:  

### Server side
1. Create one or more servers for a task in multiple terminals in the parent directory by:    
`$ celery worker --app=celery_test.celeryapp:app --loglevel=info -Q add`     

### Client Side 
In another terminal:   
1. Run the flask server in the parent directory by:
```$ python initial.py```   
2. Open the flask server at `localhost:5000`. 
3. Create the file which you want to execute as a ".txt" file. The file must contain 2 space separated numbers in multiple lines.
4. Select the task and upload the file.   


## Flow of the code 

The basic flow of the code is as follows: 
1. The client interacts with a webpage for uploading tasks, which is connected to a Flask backend. This Flask backend can host any number of clients and can be connected to multiple servers which run our tasks (called workers) at a time.   

The client uploads a file with a task.    

2. Once a task is received by Flask, it automatically forwards it to a celery worker which runs remotely. These workers can be made to run for multiple tasks or for a single task.    

3. The celery worker executes the task and outputs the result in the output file, which is automatically downloaded on the client. Flask plays a large role in connecting the client and the worker which executes the task. Flask acts as the middleware in this case.    

Please feel free to reach out in case of any questions.    

## Demonstration Video: Fault Tolerance and Load Balancing 
1.  Video 1 (Client side usage)
2. Video 2 (Load Balancing)
3. Video 3 (Worker: Failure and Recovery)
4. Video 4 (Worker: Works even when the other worker fails in Video 3):  
The small pause in the video was when the server tried to retry connection with the other server which failed and reallocate the tasks which were currently started by the other server but was not able to complete. This attribute shows the fault tolerant approach of the project. 
**Link:** https://drive.google.com/drive/folders/14wI51kcO9MGOCTzZuUb0bHy-L9cotulz

## Helpful resources:    
[1]: https://avilpage.com/2014/11/scaling-celery-sending-tasks-to-remote.html   
[2]: http://docs.celeryproject.org/   
[3]: https://www.rabbitmq.com/documentation.html   
[4]: http://flask.pocoo.org/docs/1.0/   
