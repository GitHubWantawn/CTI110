


def get_input():

    hours_worked = int(input("Please enter hours worked: "))

    pay_rate = int(input("Please enter pay rate: "))

    return hours_worked, pay_rate

hours, rate = get_input()

gross_pay = calc_gross(hours, rate)

def calc_gross(hours, rate):

    if hours > 40:
        over_hours = hours - 40
        over_pay = over_hours * rate * 1.5
        gross_pay = 40 * rate + over_pay

    else:
        gross_pay = hours * rate

    return gross_pay

gross_pay = calc_gross(hours, rate)

print("Your gross pay is: ", gross_pay)


