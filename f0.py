import re
def Foo(): return list(map(int, re.findall("\d+", input()))) + [0]
a, b, Func1 ,Func2= Foo(), Foo(), lambda a, b: a[0 + b] * 3600 + a[1 + b] * 60 + a[2 + b],lambda a:a[6] * 24 * 3600
Func3 = lambda a:Func1(a,3)-Func1(a,0)+Func2(a)
c = (Func3(a)+Func3(b))//2
print('%02.d:%02.d:%02.d' % (c // 3600, c % 3600 // 60, c % 60))