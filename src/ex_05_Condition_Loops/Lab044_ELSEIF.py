# Find the positive number is even or odd

num = int(input("Enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")
else:
    print("negative number")

#*******************************************************************************************
if num >= 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Negative Number")

# You can write short one-liner conditions using ternary operator: