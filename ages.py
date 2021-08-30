ages = {"julia" : 17, "monica" : 15, "sylvia": 7}

# print(ages["monica"])

def birthday(name):
    ages[name] = ages[name] + 1

print(birthday("monica"))