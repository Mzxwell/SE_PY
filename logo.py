a = [0, 0]
b = 0
c = 0
d = 1
e = ' '
f = 0
qi_pan = [[' ' for i in range(10)] for j in range(10)]
com_num = int(input())
for i in range(com_num):
    com = input()
    if com[0] == 'U':
        b = 0
        c = -1
    elif com[0] == 'D':
        b = 0
        c = 1
    elif com[0] == 'R':
        b = 1
        c = 1
    elif com[0] == 'L':
        b = 1
        c = -1
    for j in range(int(com[2])):
        a[b] += c
        if a[0] < 0 or a[1] < 0 or a[0] > 9 or a[1] > 9:
            f = 1
            break
        if len(com) == 5:
            e = com[4]
        qi_pan[a[0]][a[1]] = e
if f:
    print("Error!")
else:
    for i in range(10):
        print("".join(qi_pan[i]))