# CTI-110
# P2 - Sales Tax
# Juan Hernaez
# 02/20/2018

# Variables or user input


# Calculations

amount_of_purchase = float(input("Enter the amount of purchase: "))
state_tax = amount_of_purchase * 0.05
county_tax = amount_of_purchase * 0.025
total_sales_tax = amount_of_purchase + state_tax + county_tax


# Output

print("The amount of purchase is: ",format(amount_of_purchase, "0.2f"))
print("the state tax is: ",format(state_tax, "0.2f"))
print("The county tax is: ",format(county_tax, "0.2f"))
print("The total sales tax is ",format(total_sales_tax, "0.2f"))
