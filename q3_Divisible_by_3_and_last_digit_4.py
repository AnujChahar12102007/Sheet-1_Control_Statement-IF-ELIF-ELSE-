# Check if a number is divisible by 3 and last digit is 4.

n=int(input("Enter a number : "))
if (n % 10 == 4 and n % 3 == 0):
    print("Number is satisfied with query")
else:
    print("No number is not satisfied with query")