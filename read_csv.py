import csv
def getcommand(file):
    com_num = int(input())
    for i in range(com_num):
        com = input()
        if com[0] == 'I':
            f = open(file, "a")
            f.write('\n' + com[7:len(com)])
        if com[0] == 'S':
            with open(file, 'r') as f:
                table, date, max_salary, max_len = csv.reader(f), [], 0, [0,0]
                for row in table:
                    date.append(row)
                    max_salary += int(row[2])
                for k in range(2): max_len[k] = max(k+4,max(len(l0[k]) for l0 in date))
                date.sort(key=lambda x: int(x[2]))
                print('{0: <{1[0]}} {2: <{1[1]}} {3}'.format("Name", max_len, "Title", "Salary"))
                for row in date: print(  '{0[0]: <{1[0]}} {0[1]: <{1[1]}} {2}'.format(row, max_len, "{:.2f}".format(float(row[2]))))
                print('AVG:%.2f' % (max_salary / len(date)))
getcommand('a.csv')