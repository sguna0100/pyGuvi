lst1=["[","{","("] 
lst2=["]","}",")"] 
s=input()
stack=[] 
for i in s: 
    if i in lst1: 
        stack.append(i) 
    elif i in lst2: 
        pos = lst2.index(i) 
        if ((len(stack) > 0) and
            (lst1[pos] == stack[len(stack)-1])): 
            stack.pop() 
        else: 
            print("unbalanced")
if len(stack) == 0: 
    print("balanced")
