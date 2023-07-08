times = int(input())
for i in range(times):
    s, t, flag = input(), input(), True
    k = [-1] * len(t)
    while flag:
        k[0] += 1
        if k[0] >= len(s): flag=False
        for j in range(1, len(t)):
            k[j] = 1 + k[j - 1]
            if k[j] >= len(s):break
            while k[j] < len(s) and t[j] != s[k[j]]: k[j] += 2
        if k[len(k) - 1] < len(s) and t[len(t) - 1] == s[k[len(k) - 1]] and (len(s)-k[len(k) - 1]-1)%2 ==0 and t[0]==s[k[0]]:break
    if flag:print("YES")
    else:print("NO")