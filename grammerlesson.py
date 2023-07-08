sentence, end, num = input().split(), ['lios', 'inites', 'etr', 'etra', 'initis', 'liala'], [1, -1, 2, -2, 3, -3, 0]
num_sen = list(map(lambda a: ([num[end.index(i)] for i in end if a.endswith(i)] + [0])[0], sentence))
print('YES') if ((all(
    num_sen[i] <= num_sen[i + 1] and num_sen[i] * num_sen[i + 1] > 0 for i in range(len(num_sen) - 1)) and (
                              num_sen.count(2) == 1 or num_sen.count(-2) == 1)) if len(sentence) > 1 else num_sen[
    0]) else print('NO')
