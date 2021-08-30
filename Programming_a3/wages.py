def pay(wage, hours):
    extra_hours = hours - 40
    if extra_hours <= 0:
        return wage * hours
    else:
        return ((1.5 * wage) * extra_hours) + (wage * (hours - extra_hours))

def pay_table(wage, hours_list):
    for i in range (len(hours_list)):
        hours = hours_list[i]
        print("Week ", (i + 1), " : ", pay(wage, hours)) 






