# WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.


Num = int(input("Enter a number (1 to 7): "))
if Num == 1:
    print("Sunday")
elif Num == 2:
    print("Monday")
elif Num == 3:
    print("Tuesday")
elif Num == 4:
    print("Wednesday")
elif Num == 5:
    print("Thursday")
elif Num == 6:
    print("Friday")
elif Num == 7:
    print("Saturday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")

