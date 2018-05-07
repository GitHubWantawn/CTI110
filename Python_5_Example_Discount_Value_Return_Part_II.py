

def main():

    price = get_price()

    sales_price = price - discount(price)

    print("The sales price is: ", sales_price)


def get_price():

    price = int(input("Please enter the price: "))

    return price

def discount(price):

    sales = price * .10

    return sales


main()
