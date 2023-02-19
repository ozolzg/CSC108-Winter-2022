# Q1
input_list = list(map(int, input().split(' ')))
diff = 0
is_first = True

for i in range(len(input_list) + 1):
    for j in range(i):
        sublist = input_list[j: i]
        if len(sublist) <= 1:
            continue

        min_value = 0
        max_value = 0
        is_first_sublist = True

        for k in range(0, len(sublist)):
            val = sublist[k]
            if val < 1 or val > 10 ** 9:
                continue

            if is_first_sublist:
                min_value = val
                max_value = val
                is_first_sublist = False
                continue

            if min_value > val:
                min_value = val

            if max_value < val:
                max_value = val

        if is_first:
            diff = max_value - min_value
            is_first = False
        else:
            if diff > (max_value - min_value):
                diff = max_value - min_value
print(diff)