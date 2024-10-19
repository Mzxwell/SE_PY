B = ["a", "b"]
c_star = set()
n = int(input())


def f(x, y):
    return f"f({x}, {y})"


def g(x):
    return f"g({x})"


def h(x):
    return x


def build(set0):
    if n == len(set0):

        c_star.add(set0[-1])
        return
    if set0:
        for x in set0:
            for y in set0:
                if f(x, y) not in set0:
                    build(set0 + [f(x, y)])
            if g(x) not in set0:
                build(set0 + [g(x)])
    for element in B:
        if element not in set0:
            build(set0 + [element])


build([])
my_list = list(c_star)
for i in range(0, len(my_list), 5):
    print(", ".join(my_list[i:i + 5]))
print(len(c_star))
