# CTI-110
# P2 Exercises - Sales Price
# Juan Hernaez
# 02/20/2018
#

original_price = float(input("Price entered by the user: "))
discount_price = original_price * 0.20
sales_price = original_price - discount_price

print("The original price is: ",format(original_price, '0.2f'))
print("The discount price is: ",format(discount_price))
print("The sales price is: ",format(sales_price))
