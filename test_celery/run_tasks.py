from .tasks import longtime_add
# from .tasks import longtime_add, username_password_generator
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    # result = username_password_generator.delay(9)
    print("Task finished?" + str(result.ready()))
    print("Task result: " + str(result.result))
    time.sleep(10)
    print("Task finished?" + str(result.ready()))
    print("Task result: " + str(result.result))