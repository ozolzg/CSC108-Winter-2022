d = list(map(int, input().split()))  # car
e = list(map(int, input().split()))  # garage

travel = 0
for car in range(0, len(d)):
    val = 0
    min_value = 0
    first = True
    for garage in range(0, len(e)):
        val = abs(e[garage] - d[car])

        if first:
            min_value = val
            first = False
            continue

        if min_value > val:
            min_value = val
    travel += min_value

print(travel)
