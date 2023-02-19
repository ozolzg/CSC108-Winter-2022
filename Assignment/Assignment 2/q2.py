string = input().split(' ')
x = int(string[0])
y = int(string[1])

if x > 500 or x < 0:
    print("Error : (x > 500 or x < 0) is true then program exit")
    quit()

if y > 500 or y < 0:
    print("Error : (y > 500 or y < 0) is true then program exit")
    quit()

box = [[0 for i in range(0, y)] for j in range(0, x)]

commands = []
for i in range(0, y):
    string = input().split(" ")
    commands.append(string)


g = 0
for i in range(0, len(commands)):
    cmd = int(commands[i][0])
    if cmd == 1:
        r = int(commands[i][1]) - 1
        c = int(commands[i][2]) - 1
        box[r][c] = 1
    if cmd == 2:
        r1 = int(commands[i][1]) - 1
        c1 = int(commands[i][2]) - 1
        r2 = int(commands[i][3]) - 1
        c2 = int(commands[i][4]) - 1
        if r2 < r1 or c2 < c1:
            continue
        for ii in range(r1, r2+1):
            for jj in range(c1, c2+1):
                if int(box[ii][jj]) == 1:
                    g += 1

print(g)
