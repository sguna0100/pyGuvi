n=int(input())
a=[int(i) for i in input().split()]
print(a.index(min(a[:n]))+1,a.index(max(a[:n]))+1)
