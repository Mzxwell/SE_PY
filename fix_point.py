import mpmath

mpmath.mp.dps = 10000
a = int(input())
x = mpmath.mpf('0.4')
for i in range(a):
    x = (1 - x * x) / 2
print(str(x))
