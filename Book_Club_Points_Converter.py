# CTI-110: Book Club Points
# Juan Hernaez
# 03/01/2018

# Define variables and/or get user input

books = int(input("Enter number of book(s): "))

# Calculations or decision structure

if books == 0 or books == 1:
    print("The number of points earned is 0.")
elif books == 2 or books == 3:
    print("The number of points earned is 5.")
elif books == 4 or books == 5:
    print("The number of points earned is 15.")
elif books == 6 or books == 7:
    print("The number of points earned is 30.")
elif books == 8 or books == 9:
    print("The number of points earned is 60.")
elif books > 9:
    print("The number of points earned is 60.")

# Display results
