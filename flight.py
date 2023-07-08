import re

cha1 = [0, 0, 0]
cha2 = [0, 0, 0]
ave = [0, 0, 0]
a = re.findall("\d+", input())
b = re.findall("\d+", input())
num_a = list(map(int, a))
num_b = list(map(int, b))

cha1[2] = num_a[5] - num_a[2]
cha1[1] = num_a[4] - num_a[1]
cha1[0] = num_a[3] - num_a[0]
cha2[2] = num_b[5] - num_b[2]
cha2[1] = num_b[4] - num_b[1]
cha2[0] = num_b[3] - num_b[0]

if len(num_a) == 7:
    cha1[0] += 24 * num_a[6]
if len(num_b) == 7:
    cha2[0] += 24 * num_b[6]

ave[0] = cha1[0] + cha2[0]
ave[1] = cha1[1] + cha2[1]
ave[2] = cha1[2] + cha2[2]

if ave[2] < 0:
    ave[2] += 60
    ave[1] -= 1

if ave[1] < 0:
    ave[1] += 60
    ave[0] -= 1

for x in range(len(ave)):
    if ave[x] % 2 == 0:
        ave[x] /= 2
    else:
        if x < 2:
            ave[x] -= 1
            ave[x] /= 2
            ave[x + 1] += 60
        else:
            ave[x] /= 2

if ave[2] >= 60:
    ave[2] -= 60
    ave[1] += 1

print('%02.d:%02.d:%02.d' % (ave[0], ave[1], ave[2]))