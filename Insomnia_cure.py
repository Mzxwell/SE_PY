k = 0
damage = [0] * 4
for i in range(4):
    damage[i] = int(input())
total = int(input())
for i in range(1, total + 1):
    for j in range(4):
        if i % damage[j] == 0:
            k += 1
            break
print(k)
