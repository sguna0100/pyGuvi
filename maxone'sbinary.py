n=int(input())
_max=0
while n>0:
    n &=(n<<1)
    _max += 1
print(_max)
