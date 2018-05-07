# Test average
# Juan Hernaez
# 02/22/2018

# Define variables or get input

score_1 = float(input("Please enter first score: "))
score_2 = float(input("Please enter second score: "))
score_3 = float(input("Please enter third score: "))

# Calculations or decisions

average = (score_1 + score_2 + score_3) / 3
if average > 95:
    print("Congratulations!")
else:
    print("Study harder next time!")


# Output or dispaly results

print("The average of the three scores is: ", average)
                
