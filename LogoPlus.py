import re

a = [0, 0]
b = 0
c = 0
f = 0
qi_pan = [[' ' for i in range(10)] for j in range(10)]


def direction(direct):
    nonlocal a, b, c
    if direct == 'U':
        b = 0
        c = -1
    elif direct == 'D':
        b = 0
        c = 1
    elif direct == 'R':
        b = 1
        c = 1
    elif direct == 'L':
        b = 1
        c = -1
    return


def move0(direct, num, word):
    nonlocal f
    direction(direct)
    for j in range(num):
        a[b] += c
        if a[0] < 0 or a[1] < 0 or a[0] > 9 or a[1] > 9:
            f = 1
            return
        qi_pan[a[0]][a[1]] = word
    return


def move(direct, num):
    nonlocal f
    direction(direct)
    a[b] += c * num
    if a[0] < 0 or a[1] < 0 or a[0] > 9 or a[1] > 9:
        f = 1
        return
    return


com = re.split(' +', input())
while com[0] != "end":
    if len(com) < 4:
        com.append(' ')
    if com[0] == "move":
        move0(com[1], int(com[2]), com[3])
    if com[0] == "pen_up":
        com = list(input().split(" "))
        while com[0] != "pen_down":
            move(com[1], int(com[2]))
            if f == 1:
                break
            com = re.split(' +', input())
    if com[0] == "rect":
        move0('R', int(com[1]) - 1, com[3])
        move0('D', int(com[2]) - 1, com[3])
        move0('L', int(com[1]) - 1, com[3])
        move0('U', int(com[2]) - 1, com[3])
    if com[0] == "rect_f":
        for i in range(int(com[2])):
            qi_pan[a[0]][a[1]] = com[3]
            move0('R', int(com[1]) - 1, com[3])
            if f == 1:
                break
            move('L', int(com[1]) - 1)
            if i < int(com[2]) - 1:
                move('D', 1)
        move('U', int(com[2]) - 1)
    if com[0] == "cross":
        qi_pan[a[0]][a[1]] = com[2]
        move0('R', int(com[1]), com[2])
        move('L', int(com[1]))
        move0('D', int(com[1]), com[2])
        move('U', int(com[1]))
        move0('L', int(com[1]), com[2])
        move('R', int(com[1]))
        move0('U', int(com[1]), com[2])
        move('D', int(com[1]))
    com = re.split(' +', input())
if f:
    print("Error!")
else:
    for i in range(10):
        print("".join(qi_pan[i]))
