a = int(input())
b = int(input())

b1 = b // 100;
b2 = (b % 100) // 10;
b3 = (b % 100) % 10;

print(a * b3)
print( a * b2)
print( a * b1)
print( a * b)