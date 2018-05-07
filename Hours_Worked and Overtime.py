# Hours Worked and Overtime
# Juan Hernaez
# 02/22/2018

# Define variables or get input

hours_worked = int(input("Enter hours worked: "))
hourly_rate = int(input("Enter hourly rate: "))

# Calculations or decisions

if hours_worked > 40:
    print ("Over")
    ot_hours = hours_worked - 40
    reg_pay = 40 * hourly_rate
    ot_pay = ot_hours * hourly_rate * 1.5
    gross_pay = reg_pay + ot_pay
    print ("You will be paid $ ", gross_pay)


else:
    gross_pay = hours_worked * hourly_rate
    print("You will be paid $ ", gross_pay)

