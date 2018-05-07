# Programming Exercise 3

# Global constants for calories
CALORIES_FROM_FAT = 9
CALORIES_FROM_CARBS = 4


# Get grams fat.
gramsFat = float(input('Enter the fat grams consumed: '))

# Get grams carbs.
gramsCarbs = float(input('Enter the carbohydrate grams consumed: '))



def calcFatCarbs(gramsFat, gramsCarbs):

    caloriesFat= gramsFat * CALORIES_FROM_FAT 


    caloriesCarbs = gramsCarbs * CALORIES_FROM_CARBS

    return caloriesFat, caloriesCarbs



# Calculate calories from fat.
# Calculate calories from carbs.
caloriesFat , caloriesCarbs = calcFatCarbs(gramsFat, gramsCarbs)

# Print calories.
# The showCarbs function accepts the number of grams of fat and
# of carbs, as well as the calories from fat and from carbs, as
# arguments and displays the resulting calories.

print('Grams of fat: ', format(gramsFat, '.2f'))
print('Fat calories: ', format(caloriesFat, '.2f'))
print('\nGrams of carbs: ', format(gramsCarbs, '.2f'))
print('Carb calories: ', format(caloriesCarbs, '.2f')) 

