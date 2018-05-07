temp = int(input("Enter temperature: "))

while temp >= 100:

    print("Temperature is too high!\"n",\
          "Turn thermometer down and take temperature again in 5 minutes.")

    temp = int(input("Enter new temperature: "))

print("Temperature is acceptable.")
