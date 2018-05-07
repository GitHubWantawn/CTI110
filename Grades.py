# CTI-110 Scores Grades
# Juan Hernaez
# 02/27/2018

# Define variables and/or get user input

grade = int(input("Enter grade: "))

# Calulations or decision structure

if grade >= 90:
    print("Your grade is an A")
else:
    if grade >= 80:
        print("Your grade is a B")
    else:
        if grade >= 70:
            print("Your grade is a C")
        else:
            if grade >= 60:
                print("Your grade is a D")
            else:
                if grade < 60:
                    print("Your grade is an F")
                    
        
