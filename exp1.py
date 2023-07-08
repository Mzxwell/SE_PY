import csv
com = "INSERT Happy,staff,30000"
f = open('a.csv', "a")
f.write('\n')
f.write(com[7:len(com)])
f.close()
with open("a.csv", "r") as a:
    f = csv.reader(a)
    date = []
    for row in f:
        date.append(row)
    max_len = [0] * 3
for k in range(3):
    max_len[k] = max(len(l0[k]) for l0 in date)
date.sort(key=lambda x: int(x[2]))
for row in date:
    print('{0[0]: <{1[0]}} {0[1]: <{1[1]}} {0[2]: <{1[2]}}'.format(row, max_len))
print(max_len)
