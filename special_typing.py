times = int(input())
for i in range(times):
    s, t, flag = input(), input(), True
    k = [0] * len(t)
    if (len(s) - len(t)) % 2 != 0: k[0] = 1
    while flag:
        for j in range(0, len(t)):
            if j > 0:
                k[j] = 1 + k[j - 1]
            if k[j] >= len(s):
                flag = False
                break
            while k[j] < len(s) and t[j] != s[k[j]]:
                k[j] += 2
        if k[len(k) - 1] < len(s) and t[len(t) - 1] == s[k[len(k) - 1]]:
            break
        else:
            k[0] += 2
    if flag:
        print("YES")
    else:
        print("NO")
