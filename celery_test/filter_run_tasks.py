from .tasks import longtime_multiply
import time
import os
from os.path import dirname,abspath
import numpy as np
from numpy import asarray
import time
import cv2
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from PIL import Image
#if __name__ == '__main__':
file_path = dirname(dirname(abspath(__file__)))
# print(file_path)
upload_folder = file_path+"/celery_test/Uploads"
output_folder = file_path+"/celery_test/Outputs"
f = os.listdir(upload_folder)[0]
fh = plt.imread(file_path+"/celery_test/Uploads/"+f)
num_val = len(fh.flatten())
res_out = np.zeros((num_val,),dtype=bool)
if os.listdir(output_folder) :
    os.unlink(output_folder+"/"+os.listdir(output_folder)[0])
start = time.clock()
start1 = time.time()
start2 = timer()
ressult = []

for f in os.listdir(upload_folder):
    ct = 0
    m = plt.imread(upload_folder+"/"+f)
    m1 = m[:,:,:]
    new_m1 = m1.copy()
    h,w, c = np.shape(m1)
    p= 10
    p = p/100
    for i in range(h):
        for j in range(w):
            for k in range(c):
                result =  longtime_multiply.delay(int(new_m1[i][j][k]),float(p))
                if result.ready()==True:
                    res_out[ct] = True
                    new_m1[i][j][k] = result.result
                    print(result.result)
                ct = ct+1

        
    img = Image.fromarray(new_m1, 'RGB')
    img.save(output_folder+"/"+"out.jpg")
        
res_out = np.zeros((num_lines,),dtype=bool)
elapsed = (time.clock() - start)
elapsed1 = (time.time()- start1)
elapsed2 = timer()- start2
print(elapsed)
print(elapsed1)
print(elapsed2)