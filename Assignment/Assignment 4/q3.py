# Q3
d = list(map(int, input().split(' ')))
e = int(input())  # refill

capacity = max(d)

while True:

    gas = capacity
    refill = 0
    for p in range(0, len(d)):  # p = planet
        if gas > d[p]:
            gas -= d[p]
        elif gas < d[p]:
            refill += 1
            gas += capacity
            gas -= d[p]
        elif gas == d[p]:
            gas -= d[p]
            refill += 1
            gas += capacity
            if p == len(d) - 1:
                break

    if refill <= e:
        break
    elif refill > e:
        capacity += 1

print(capacity)
