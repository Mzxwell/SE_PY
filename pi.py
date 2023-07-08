import mpmath

file = open("pi.txt", 'w')
mpmath.mp.dps = 2000000
file.write(str(mpmath.pi))
file.close()
