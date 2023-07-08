import re

f_name = input()
l_name = input()
code = input()
ID0 = input()
ID = ID0.split("-")
num = re.search("[^0-9]+", code)
ID1 = re.search("[^A-Z]+", ID[0])
if len(ID) < 2:
    ID2 = "a"
else:
    ID2 = re.search("[^0-9]+", ID[1])
if len(f_name) == 0:
    print('The first name must be filled in.')
else:
    if len(f_name) < 2:
        print('\"%s\" is not a valid first name. It is too short.' % f_name)
if len(l_name) == 0:
    print('The last name must be filled in.')
else:
    if len(l_name) < 2:
        print('\"%s\" is not a valid last name. It is too short.' % l_name)
if len(code) == 0 or num is not None:
    print("The ZIP code must be numeric.")
if len(ID[0]) != 2 or len(ID[1]) != 4 or ID1 is not None or ID2 is not None:
    print("%s is not a valid ID." % ID0)
