import re

a = list(map(int, re.findall("\d+", input())))
b = -1
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j + i + 1] - a[i] > b:
            b = a[j + i + 1] - a[i]
print(b, end='')
