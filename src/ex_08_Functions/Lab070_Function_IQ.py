# Create a program to sum 3 numbers from the user input, if user does not enter any number then
# take default as 100,200,300

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter a third number: "))

def sum_of_three_nums(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

result = sum_of_three_nums(n1=20, n2=30, n3=50)
print(result)
result1 = sum_of_three_nums()
print(result1)
result2 = sum_of_three_nums(n2=100)
print(result2)
result3 = sum_of_three_nums(1,2,3)
print(result3)
result4 = sum_of_three_nums(n3=30, n2= 15)
print(result4)