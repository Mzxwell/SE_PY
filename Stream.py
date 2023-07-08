def process(param):
    i = 0
    while i < len(param):
        if len(param[i]) == 1:
            del param[i]
        else:
            param[i] = param[i].capitalize()
            i += 1
    return ",".join(param)


stream = input().split()
print(stream)
print(process(stream))
