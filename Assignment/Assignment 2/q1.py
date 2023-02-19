no_roasting = input()
no_s = input()
no_p = input()

roasting = []

for i in range(0, int(no_roasting)):
    inp = input()
    tmp_r = inp.split(" ")
    r = [int(tmp_r[0]), tmp_r[1][0], int(tmp_r[1][1]), tmp_r[1], tmp_r[2][0], int(tmp_r[2][1]), tmp_r[2]]
    roasting.append(r)

s_points = 0
p_points = 0

for i in range(0, len(roasting)):

    if roasting[i][0] < 1 or roasting[i][0] > 200:
        print("Error > t_i : %d (%d)" % (i, roasting[i][0]))
        quit()

    if i != len(roasting) - 1 and roasting[i][0] > roasting[i + 1][0]:
        print("Error > t_i : %d > %d" % (roasting[i][0], roasting[i + 1][0]))
        quit()

    if roasting[i][2] < 0 or roasting[i][2] > int(no_s):
        print("Error > Number of Student")
        quit()

    if roasting[i][5] < 0 or roasting[i][5] > int(no_s):
        print("Error > Number of Professor")
        quit()

    if roasting[i][1].lower() == "s":
        s_points += 500
        j = 0
        y = i - 1
        for j in range(y, -1, -1):
            if roasting[j][3] == roasting[i][3]:
                if (roasting[i][0] - roasting[j][0]) <= 10:
                    s_points += 500

    elif roasting[i][1].lower() == "p":
        p_points += 500
        j = 0
        y = i - 1
        for j in range(y, -1, -1):
            if roasting[j][3] == roasting[i][3]:
                if (roasting[i][0] - roasting[j][0]) <= 10:
                    p_points += 500

print("%d %d" % (s_points, p_points))
