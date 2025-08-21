# Accept the percentage from the user and display the grade according to criteria.

English = int(input("Enter the grade of the English : "))
Hindi = int(input("Enter the grade of the Hindi : "))
Maths = int(input("Enter the grade of the Maths : "))
Total = English + Hindi + Maths
percentage = (Total / 300) * 100

if percentage >= 80.0:
    print("Student obtaained GRADE A")
elif percentage >= 70 and percentage < 80:
    print("Student obtaained GRADE B")
elif percentage >= 60 and percentage < 70:
    print("Student obtaained GRADE C")
elif percentage >= 40 and percentage < 60:
    print("Student obtaained GRADE D")
else:
    print("Student obtaained GRADE E")
