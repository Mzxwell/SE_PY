import time

thisyear = int(time.strftime("%Y", time.localtime()))
print(thisyear)
ghj = ['dfdjk', 'dfs', 'dasf']
jhj = ghj
jkhkj = ghj[:]
print(ghj)
del ghj[1]
print(ghj, '\n', jhj, '\n', jkhkj)
