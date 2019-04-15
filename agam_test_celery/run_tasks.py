from .tasks import longtime_add
import time
import os
from os.path import dirname,abspath
if __name__ == '__main__':
    file_path = dirname(dirname(abspath(__file__)))
    for f in os.listdir(file_path+"/flask_app/Uploads"):
        fh = open(file_path+"/flask_app/Uploads/"+f)
        for line in fh:
            a,b = line.split(" ")  
            result = longtime_add.delay(int(a),int(b))
            # at this time, our task is not finished, so it will return False
            print('Task finished? ', result.ready())
            print('Task result: ', result.result)   
            # sleep 10 seconds to ensure the task has been finished
            time.sleep(10)
            # now the task should be finished and ready method will return True
            print('Task finished? ', result.ready())
            print('Task result: ', result.result)
            f_out = open(file_path+"/Outputs/"+"out.txt","a+")
            f_out.write(str(result.result)+"\n")
        fh.close()
        f_out.close()
        