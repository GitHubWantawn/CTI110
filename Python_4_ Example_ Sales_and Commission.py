# CTI 110
# Python Four Example: Sales and Commission
# Juan Hernaez
# 03/08/2018

# Set value of keep_going to y so loop iterates at least once:

keep_going = "y"

while keep_going == "y":
    sales = float(input("Enter sales amount: "))

    commission_rate = float(input("Enter commission rate: "))

    commission = sales * commission_rate

# Display commission calculted:

    print("Your commission is", commission)

    print() # To skip a line.

# Below statement provides means to terminate loop or to continue:

    keep_going = input("Do you want to calculate another commission? Enter y if yes.")

    print()
    
