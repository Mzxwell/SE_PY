a, b, c = input(), [], []
while a != '':
    b.append(list(map(int, a.split()))[0])
    c.append(list(map(int, a.split()))[1])
    a=input()
for i in range(len(b)):
    print(b[i] + c[i])
