import time
import sys

c = int(input("input a number n to calculate fib(n):"))
start = time.perf_counter()
sys.set_int_max_str_digits(0)
a = 1
b = 1
if c > 2:
    for i in range(c - 2):
        trans = a + b
        a = b
        b = trans
    print("fib(%d) = %d" % (c, b))
else:
    print("fib(%d) = %d" % (c, b))
end = time.perf_counter()
print(end - start)
