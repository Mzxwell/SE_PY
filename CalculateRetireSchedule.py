import time

this_year = int(time.strftime("%Y", time.localtime()))
age_n = int(input("What is your current age?"))
age_r = int(input("At what age would you like to retire?"))
years = age_r - age_n
if years < 0:
    print("You have 0 years left until you can retire.")
else:
    print("You have %d years left until you can retire." % years)
print("It's %d, so you can retire in %d." % (this_year, this_year + years))
