from .tasks import longtime_multiply, longtime_add
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
a1,a2,a3 = fh.shape
num_val = (a1-4)*(a2-4)*a3
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
    h,w, channels = np.shape(m1)
    z1 = np.ones((5,5))
    z1 = 0.00009*z1  
    b1 = h - 4
    c1 = w - 4
    new_m1 = np.zeros((b1,c1,channels))
    for b in range(b1):
        for c in range(c1):
            for k in range(channels):
                for d in range(5):
                    for e in range(5):
                        A = longtime_multiply.delay(z1[d][e],m1[b+d][c+e])
                        result = longtime_add.delay(ac[b][c], A.result)
                        new_m1[b][c][k] = result.result
                if result.ready()==True:
                    res_out[ct] = True
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