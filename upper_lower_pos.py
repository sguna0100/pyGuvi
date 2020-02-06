s=input()
t=int(input())
p=int(input())
l='0'
l+=s
li=''
if t==1:
    for i in range(len(s)+1):
        if i%p==0:
            li+=l[i].lower()
        else:
            li+=l[i]
if t==2:
    for i in range(len(s)+1):
        if i%p==0:
            li=l[i].upper()
        else:
            li+=l[i]
print(li[1:])
