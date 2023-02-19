max_weight = float(input())
a = float(input())
b = float(input())
c = float(input())

if (a > max_weight) and (b > max_weight) and (c > max_weight):
    print("TOO HEAVY")
elif (a < max_weight) and (b < max_weight) and (c < max_weight):
    print("ALL CLEAR")
else:
    print("FINE")

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)
