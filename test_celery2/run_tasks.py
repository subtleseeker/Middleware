from .tasks import longtime_add
from .tasks import longtime_add, username_password_generator, multiplication, matrix_multiplication
import time

# TASK: get these variables dynamically from the form and the file
task = "addition"
# task = "userpass"
x = 2
y = 100000000000004

if __name__ == '__main__':
    if task == "addition":
        result = longtime_add.delay(x,y)
    elif task == "userpass":
        result = username_password_generator.delay(x)
    elif task == "matmul":
        pass
    elif task == "multiplication":
        pass
        

    print(result)

    # TASK: result.result doesn't return our tuple in userpass. It returns 'test_celery.tasks.username_password_generator'. Why?

    print("Task finished? " + str(result.ready()))
    print("Task result: " + str(result.result))
    time.sleep(10)
    print("Task finished? " + str(result.ready()))
    print("Task result: " + str(result.result))
    print(type(result.result))
    print(type(result))