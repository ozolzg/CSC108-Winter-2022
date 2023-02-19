# Q4
c = input().split(' ')
# c = ["green", "red", "red", "blue", "red", "red", "green"]
# c = ["red", "red", "green", "green", "blue", "red"]
# c = ["red", "green", "blue"]
# c = ["r", "g", "z", "g", "b", "b", "r", "r", "g", "y", "g", "g", "y", "b"]

colors = {}
is_first = True

for i in range(len(c) + 1):
    for j in range(i):
        sublist = c[j: i]

        no_colors = len(set(sublist))
        len_sublist = len(sublist)

        if no_colors in colors:
            if colors[no_colors] > len_sublist:
                colors[no_colors] = len_sublist
        else:
            colors[no_colors] = len_sublist

t = list(map(str, colors.values()))
print(' '.join(t))
