# WAP to check if the number is divisible by 7 or if the last digit is 5.

n=int(input("Enter a number : "))
if (n % 10 == 5 or n % 7 == 0):
    print("Number is divisible by 7 and last digit is 4")
else:
    print("Number is not satisfied with query")