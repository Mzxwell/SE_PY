import re
a = list(map(int, re.findall("\d+", input())))
b = list(map(int, re.findall("\d+", input())))
if len(a) == 6: a.append(0)
if len(b) == 6: b.append(0)
c = a[3] * 3600 + a[4] * 60 + a[5] - (a[0] * 3600 + a[1] * 60 + a[2]) + a[6] * 24 * 3600
d = b[3] * 3600 + b[4] * 60 + b[5] - (b[0] * 3600 + b[1] * 60 + b[2]) + b[6] * 24 * 3600
ave = (d + c) // 2
print('%02.d:%02.d:%02.d' % (ave // 3600, ave % 3600 // 60, ave % 60))