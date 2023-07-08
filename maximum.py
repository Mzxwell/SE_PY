a,b = list(map(int, input().split())),-1
for i in range(len(a) - 1):
    if(i==0 or (a[i]<a[i-1] and a[i]<a[i+1])):
        for j in range(len(a) - 1 - i):
            if a[j + i + 1] - a[i] > b:b = a[j + i + 1] - a[i]
    else:continue
print(b, end='')