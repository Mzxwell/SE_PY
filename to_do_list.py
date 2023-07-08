"""write your code in following methods"""
file_path = './tasks.txt'


def to_do():
    import re

    def add(task):
        f = open(file_path, "a")
        for i in task:
            f.write('todo:' + i + '\n')
        f.close()

    def delete(task):
        lines = [i for i in open(file_path, 'r') if all(j not in i for j in task)]
        f = open(file_path, 'w')
        f.writelines(lines)
        f.close()

    def complete(task):
        file_data = ""
        with open(file_path, "r") as f:
            for line in f:
                if any(j in line for j in task):
                    line = line.replace('todo', 'completed')
                file_data += line
        with open(file_path, "w") as f:
            f.write(file_data)

    def find(task):
        with open(file_path, "r") as f:
            for line in f:
                if task in line: print(line,end='')

    def all0():
        with open(file_path, "r") as f:
            for line in f: print(line,end='')

    com = input()
    while com != "todo -quit":
        if com[6:8] == 'a ':
            add(re.findall(r'"(.*?)"', com[8:]))
        elif com[6:8] == 'd ':
            delete(re.findall(r'"(.*?)"', com[8:]))
        elif com[6:8] == 'c ':
            complete(re.findall(r'"(.*?)"', com[8:]))
        elif com[6:8] == 'f ':
            find(com[8:])
        elif com[6:8] == 'al':
            all0()
        com = input()
    return


to_do()
