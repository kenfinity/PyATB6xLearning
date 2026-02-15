def odd_even(num):
    if num % 2 == 0:
        print("Number is even")
    else   :
        print("Number is odd")

odd_even(4)
odd_even(5)


user_input = int(input("Enter the number"))

res_l = lambda num: "even" if num % 2 == 0 else "odd"


print(res_l(user_input))

