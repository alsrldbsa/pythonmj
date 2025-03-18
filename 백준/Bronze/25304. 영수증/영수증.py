a = int(input())
b = int(input())
e = 0
for i in range(0,b):
    c,d = map(int,input().split())
    e = e+(c*d)
if e == a:
    print('Yes')
else:
    print('No')