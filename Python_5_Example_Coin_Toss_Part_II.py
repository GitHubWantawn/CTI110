# CTI-110
# Python 5 - Example - Coin Toss: Part II
# Juan Hernaez
# 04/12/2018

# Use the random module:

import random

# Set constant values:

HEADS = 1
TAILS = 2
TOSSES = 5

def main():

    for toss in range(TOSSES):

        # Simulate coin toss:

        num = random.randint(HEADS, TAILS)

        # Print the results:

        if num == HEADS:
            print("Heads!")
            
        else:
            print("Tails!")

# Call the main() function:

main()
