# CTI-110 Salary, Loan and Years on Job
# Juan Hernaez
# 02/27/2018

# Define Variables and/or get user input

salary = int(input("Enter salary: "))
years_on_the_job = int(input("Enter years on the job: "))

# Calculations or decision structure

if salary >= 30000 and years_on_the_job >= 2:
    print("You qualify for the loan.")

else:
    print("You don't earn enough.")
