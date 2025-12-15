# User Defined
# 1. They can't return - non return
# 2. They can return something
# 3. They have parameters
# 4. They don't have parameters / arguments

#built in function
result = max(3,4)
print(result)

# 1. They can't return - non return
#    No return type and no Parameter/Argument - NRNP

def greet():
    print("Hello Test")

greet()

#  2. They can't return - non return
# #    No return type but has Parameter/Argument

def greet_by_name(name):
    print("Hello " + name)

greet_by_name("John")

#  3. No return type and with default argument (# positional argument)

def say_hello_default_arg(name="Ken"):
    print("Hello ", name.upper())

say_hello_default_arg()
say_hello_default_arg("Ben")

def multiple_args(name1="Lionel", name2="Messi"):
    print("Multiple argumentsb ->",name1, name2)

multiple_args()
multiple_args("Cole", "Parmer")
multiple_args(name1="Cristiano", name2="Ronaldo")
multiple_args(name1="Eden")
multiple_args(name2="Hazard")

# 4. Argument + return Type

def sum(a, b):
    return a + b

result = sum(3, 4)
print(result)

def sum_with_default(num1=2, num2=3):
    print(f"SUM of 2 numbers {num1} and {num2}\n")
    return num1 + num2

result = sum_with_default(3, 4)
print(result)
result = sum_with_default()
print(result)