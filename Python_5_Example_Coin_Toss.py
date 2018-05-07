# CTI-110
# Python 5 - Example - Coin Toss
# Juan Hernaez
# 03/27/2018

# Use the random module:

import random

# Set constant values:

HEADS = 1
TAILS = 2

def main():

    times = int(input("Number of times to flip the coin? " ))
    for flip in range(times):

        # Simulate the coin toss:

        coin = random.randint(HEADS, TAILS)

        # Print the result:

        if coin == HEADS:
            print("Heads.")

        else:

            print("Tails.")

# Call the main() function:

main()
