# CTI-110
# Python 5 Example - dice.py - Simulates rolling dice
# Juan Hernaez
# 03/27/2018

# Use the random module:

import random

# Set constant values for minimum, maximum (dice go from 1 to 6):

MIN = 1
MAX = 6

def main():

    # Use a variable to control the loop:

    again = 'y'

    # Until the user is finished, repeat:

    while again == 'y' or again == 'Y':

        # Simulate rolling the dice:

        print("Rolling two dice...")

        first = random.randint(MIN, MAX)
        second = random.randint(MIN, MAX)
        print("Their values are: ", first, second)

        # Roll again?

        again = input('Roll again? (y = yes): ')

# Call the main() function:

main()
