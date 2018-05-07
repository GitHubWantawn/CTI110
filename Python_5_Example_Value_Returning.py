


def main ():

    reg_price = get_price()

    sales_price = reg_price - discount(reg_price)

    print(sales_price)


def get_price():

    price = int(input("Please enter price: "))

    return price

def discount(price):

    discount = price * 0.10


    return discount







main()
