# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

num1 = float(input("Enter another number: "))
num2 = float(input("Enter another number: "))
num3 = float(input("Enter another number: "))

if num1 >= num2 and num1 >= num3:
    print("Maximum", num1)
elif num2 >= num1 and num2 >= num3:
    print("Maximum", num2)
elif num3 >= num1 and num3 >= num2:
    print("Maximum", num3)