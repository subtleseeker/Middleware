from .tasks import longtime_mul
import time

if __name__ == '__main__':
    result = longtime_mul.delay(3,2)
    print("Task finished?" + str(result.ready()))
    print("Task result: " + str(result.result))
    time.sleep(10)
    print("Task finished?" + str(result.ready()))
    print("Task result: " + str(result.result))