a = list(input())
b = list(input())
f = 1
if len(a) == len(b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                del b[j]
                break
            if j == len(b) - 1:
                f = 0
        if f == 0:
            break
if f == 1:
    print("True")
