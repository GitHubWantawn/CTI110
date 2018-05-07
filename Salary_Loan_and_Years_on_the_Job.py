# CTI-110 - Salary, Loan and Year on the Job
# Juan Hernaez
# 02/27/2018

# Define variables and/or get user input

salary = int(input("Enter salary: "))
years_on_job = int(input("Enter years on job: "))


# Calculations or decision structure

if salary >=30000:
    if years_on_job >= 2:
        print("You qualify for a loan.")
    else:
        print("You must have worked for 2 years.")
else:
    print("You don't earn enough.")


# Dispaly results
