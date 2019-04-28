from .tasks import longtime_add
import time
import os
from os.path import dirname,abspath
import numpy as np
import time
from timeit import default_timer as timer
#if __name__ == '__main__':
file_path = dirname(dirname(abspath(__file__)))
# print(file_path)
upload_folder = file_path+"/celery_test/Uploads"
output_folder = file_path+"/celery_test/Outputs"
f = os.listdir(upload_folder)[0]
fh = open(file_path+"/celery_test/Uploads/"+f)
num_lines = sum(1 for line in fh)
res_out = np.zeros((num_lines,),dtype=bool)
if os.listdir(output_folder) :
    os.unlink(output_folder+"/"+os.listdir(output_folder)[0])
start = time.clock()
start1 = time.time()
start2 = timer()
ressult = []
for f in os.listdir(upload_folder):
    c = 0
    fh = open(upload_folder+"/"+f)
    f_out = open(output_folder+"/"+"out.txt","a+")
    ressult = []
    for line in fh:
        a,b = line.split(" ")
        result = longtime_add.delay(int(a),int(b))
        
        ressult.append(result)
        outt = [t.get() for t in ressult]

        if result.ready()==True:
            f_out.write(str(result.result)+"\n")
            res_out[c] = True
        c = c+1
            
    fh.close()
    f_out.close()
res_out = np.zeros((num_lines,),dtype=bool)
print(len(outt))
print(outt)
elapsed = (time.clock() - start)
elapsed1 = (time.time()- start1)
elapsed2 = timer()- start2
print(elapsed)
print(elapsed1)
print(elapsed2)