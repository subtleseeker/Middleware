import cv2
import numpy as np

m =  cv2.imread("Lena.png")
m1 = m[:,:,0]

# get image properties.
h,w,bpp = np.shape(m)
print(m) 
# print image properties.
print ("width: " + str(w))
print ("height: " + str(h))
print ("bpp: " + str(bpp))

rows = h
coloum = w 
z1 = np.ones((5,5))

z1 = 0.00009*z1

print(z1[0][0])

b1 = h - 4
c1 = w - 4
ac = np.zeros((b1,c1))

for b in range(b1):
	for c in range(c1):
		for d in range(5):
			for e in range(5):
				ac[b][c] = ac[b][c] + z1[d][e]*m1[b+d][c+e]

print(ac)
                    
cv2.imshow("image", ac);
cv2.waitKey();                  
