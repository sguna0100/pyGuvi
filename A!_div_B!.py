a,b=input().split()
a,b=int(a),int(b)
fact1=1
fact2=1
for i in range(1,a+1):
    fact1*=i
for i in range(1,b+1):
    fact2*=i
print(int(fact1/fact2))
