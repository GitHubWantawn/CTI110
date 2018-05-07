


def main():

    number = int(input("Please enter a number: "))

    Status = num(number)

    print(Status)

def num(num):

    if num % 2 == 0:

        print("Number is even.")

        status = True

    else:

        print("Number is odd.")

        status = False

    return status






main()
