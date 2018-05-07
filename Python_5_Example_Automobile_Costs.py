# CTI-110
# Python 5 Programming Exercise - Automobile Expenses
# Juan Hernaez
# 03/29/2018

# Get the amount of the loan payment:

loan = float(input("Enter the monthly loan amount: "))

# Get the amount of the insurance payment:

insurance = float(input("Enter the monthly insurance amount: "))

# Get the amount of the gas payment:

gas = float(input("Enter the monthly gas amount: "))

# Get the amount of the oil payment:

oil = float(input("Enter the monthly oil amount: "))

# Get the amount of the tires payment:

tires = float(input("Enter the monthly tires amount: "))

# Get the amount of the maintenance payment:

maintenance = float(input("Enter the monthly maintenance amount: "))


def showExpenses(loan, insurance, gas, oil, tires, maintenance):

    totalMonth = loan + insurance + gas + oil + tires + maintenance

    totalYear = totalMonth * 12


    print("Total monthly expense: $", format(totalMonth, ',.2f'),sep ='')

    print("Total annual expense: $", format(totalYear, ',.2f'),sep ='')


showExpenses(loan, insurance, gas, oil, tires, maintenance)
