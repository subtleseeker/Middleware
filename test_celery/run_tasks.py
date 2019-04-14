from .tasks import longtime_add, return_prime, multiply, upgenerator
import time
#choice = 0
#choice = int(input('Enter task choice: \n 1 for add \n 2 for prime checking \n 3 for multiplication'))
#if(choice == 1):
#    x = int(input('Enter number to be added '))
#    y = int(input('Enter number to be added'))
#    result = longtime_add.delay(x,y)
#    result.ready()
#    print('Task result: ', result.get())
#if(choice == 2):
#    x = int(input('Enter number to be checked: '))
#    result = return_prime.delay(x)
#    result.ready()
#    print('Task result: ', result.get())
#if(choice == 3):
#    x = int(input('Enter number to be multiplied: '))
#    y = int(input('Enter the other number to be multiplied'))
#    result = multiply.delay(x,y)
#    result.ready()
#    print('Task result: ', result.get())

task = "userpass"
# task = "userpass"
x = 2
y = 100000000000004
z = 2

if __name__ == '__main__':
    if task == "addition":
        result = longtime_add.delay(x,y)
    elif task == "userpass":
        result = upgenerator.delay()
    elif task == "mul":
        result = multiply.delay(x,y)
    elif task == "prime":
        result = return_prime.delay(x)
    print(result)

# TASK: result.result doesn't return our tuple in userpass. It returns 'test_celery.tasks.username_password_generator'. Why?

print("Task finished? " + str(result.ready()))
print("Task result: " + str(result.result))
time.sleep(10)
print("Task finished? " + str(result.ready()))
print("Task result: " + str(result.result))
print(type(result.result))
print(type(result))

