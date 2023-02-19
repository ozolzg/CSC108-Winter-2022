str = input().upper()

l = len(str)
row = [[" " for j in range(0, l)] for i in range(0, l)]
for i in range(0, l):
    row[0][i] = str[i]

k = len(row)
for i in range(0, k):
    for j in range(0, k-1):
        x = row[i][j]
        y = row[i][j+1]
        if y == " ":
            break
        tmp = "T"
        if x == y:
            tmp = x
        if x == "T":
            tmp = y
        if y == "T":
            tmp = x
        if x == "B":
            if y == "G":
                tmp = "S"
            if y == "D":
                tmp = "I"
        if x == "G":
            if y == "D":
                tmp = "C"
            elif y == "T":
                tmp = "G"
            else:
                tmp = "T"
        if x == "C":
            if y == "S":
                tmp = "G"
            if y == "G":
                tmp = "T"
        if x == "S":
            if y == "C":
                tmp = "G"
        if x == "I" and y == "S":
            tmp = "B"
        row[i+1][j] = tmp

print("".join(row[k-1]))

