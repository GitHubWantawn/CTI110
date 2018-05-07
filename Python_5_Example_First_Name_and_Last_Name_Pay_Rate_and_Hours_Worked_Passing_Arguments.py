

Fname = input("Please enter your first name: ")
Lname = input("Please enter your last name: ")

def dis_message(first_name, last_name):
    print("Welcome!,", first_name, last_name)

dis_message(Fname, Lname)

input("Press any key to continue\n")

pay_rate = float(input("Please enter the pay rate: "))

hours = float(input("\nPlease enter the hours worked: "))

def gross_pay(rate, hWorked):

    gross_pay = rate * hWorked

    print("\nYour gross pay is",gross_pay)

gross_pay(pay_rate, hours)
              
