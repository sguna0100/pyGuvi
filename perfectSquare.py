import math
n=int(input(int))
m=int(input(int))
o=m*n
root=math.sqrt(o)
if(int(root+0.5)**2==o):
    print("yes")
else:
    print("no")
