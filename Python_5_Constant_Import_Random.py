import random

MIN = 1

MAX = 6

def main():
    again = "y"
    while again == "Y" or again == "y":
        print("Rolling dice...\n")
        print(random.randint (MIN, MAX))
        print(random.randint (MIN, MAX))

        again = input("Do you want to play again? (Enter y if yes) ")

main()
