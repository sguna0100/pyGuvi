inpu=int(input("1.create user \n2.Login:\n"))
if inpu==1:
    a=input("enter user name:")
    c=0;h=1;up=0;lo=0;num=0;sp=0;p=''
    f=open('guvifile.txt','a')
    if '0'<=a[0] and '9'>=a[0]:h=0
    if '@' in a and '.' in a:
        c+=1
        if a.index('@')< a.index('.'):c+=1
    if c==2 and h==1:b=input("enter password:")
    else:print("INVALID USER ID...!")
    if len(b)>=5 and len(b)<=15:
        for i in b:
            if i.isupper():up=1
            if i.islower():lo=1
            if i>='0' and i<='9':num=1
            if i in '~!@#$%^&*()_+{}|:"<>?':sp=1
    if up+lo+num+sp==4:
        f.write(str(a))
        f.write('\t')
        f.write(str(b))
        f.write('\n')
        f.close()
        print('Registered...')
    else:print("INVALID PASSWORD...!")
elif inpu==2:
    a=input('Enter User Id:')
    b=input('Enter Password:')
    f=open('guvifile.txt','r')
    c=0;
    while f.readline():
        row=f.readline()
        if a in row and b in row:
            c+=1
            break 
    if c==1:print("LOG IN SUCCESSFULLY")
    else:print('INCORRECT USER AND PASSWORD.')
