x = int(input())
y = int(input())
z = int(input())

x = bool(x)
y = bool(y)
z = bool(z)

result = (x and y) or (y and z) or (x and z)

if result:
    print('ON')
else:
    print('OFF')

