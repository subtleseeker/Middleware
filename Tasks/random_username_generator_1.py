N = int(input())
M = int(input())
import random  
password = []
username = []
for x in range(N): 
    s1 = ""
    s2 = ""
      
    # print 10 random values 
    # between 1 and 100 
    for y in range(M):
        s1 = s1 + chr(random.randint(97, 122))
        z = random.randint(1,2)
        if(z  == 1):
            s2 = s2 + chr(random.randint(97,122))
        else:
             s2 = s2 + str(random.randint(1, 9)) 
    username.append(s1)
    password.append(s2)

print (username)
print (password)