f = open("/home/gaddafi/sampl.txt", "r")
line = f.readline()
num = []
while line:
    b = line.rstrip('\n')
    num.append(b)
    line = f.readline()
f.close()         
num_ints = []
for i in num:
    x = [int(l) for l in i.split(" ")]
    num_ints.append(x)

print(num_ints)    