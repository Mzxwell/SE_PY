for i in range(1, 10, 3):
    print(i)
for i in range(10):
    print(i)
for i in range(3):
    a = int(input())
    print(a * 2)
for i in range(10):
    if i % 2:
        continue
    elif i == 8:
        break
    else:
        print(i)