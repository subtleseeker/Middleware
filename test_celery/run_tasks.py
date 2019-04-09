from .tasks import longtime_add, return_prime, multiply
import time
choice = 0
choice = int(input('Enter task choice: \n 1 for add \n 2 for prime checking \n 3 for multiplication'))
if(choice == 1):
    x = int(input('Enter number to be added '))
    y = int(input('Enter number to be added'))
    result = longtime_add.delay(x,y)
    result.ready()
    print('Task result: ', result.get())
if(choice == 2):
    x = int(input('Enter number to be checked: '))
    result = return_prime.delay(x)
    result.ready()
    print('Task result: ', result.get())
if(choice == 3):
    x = int(input('Enter number to be multiplied: '))
    y = int(input('Enter the other number to be multiplied'))
    result = multiply.delay(x,y)
    result.ready()
    print('Task result: ', result.get())


