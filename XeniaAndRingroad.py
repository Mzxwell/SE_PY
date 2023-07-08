house = 1
count = 0
n, m = map(int, input().split())
a = list(map(int, input().split()))
for j in a:
    if j < house:
        count += j - house + n
    else:
        count += j - house
    house = j
print(count)
