# Given a Number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

#**************** without functions ****************
num = int(input("Enter the number: "))

fact = 1

if num < 0:
    print("Factorial does not exist for negative number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
        # print("Factorial of {} is {}".format(i, fact))
        print(f"Factorial of {i} is {fact}")


# **************** using functions ******************
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# print(fact(0))