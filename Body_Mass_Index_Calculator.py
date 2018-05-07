# CTI-110: Body Mass Index Calculator
# Juan Hernaez
# 03/01/2018

# Define variables and/or get user input

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

# Calculations or decision structure:

BMI = (weight * 703) / height ** 2
print("Your BMI is: ", BMI)

if BMI >= 18.5 and BMI <= 25:
    print("You are at an optimal weight.")
elif BMI < 18.5:
    print("You are underweight.")
elif BMI > 25:
    print("You are overweight.")


# Display results


