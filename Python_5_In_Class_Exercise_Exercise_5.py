# Programming Exercise 5

import random

# main function
def main():
    # Local variables
    oddCounter = 0
    evenCounter = 0
    totalNumbers = 10

    for counter in range(totalNumbers):

        

        # get random number
        currentNumber = random.randint(1, 100)

        print(currentNumber)

        # Check whether number is odd or even
        if currentNumber % 2 == 0:
            evenCounter+=1
        else:
            oddCounter+=1

    print ('Out of', totalNumbers, 'random numbers,', oddCounter,'were odd, and', evenCounter, 'were even.')


# Call the main function.
main()


