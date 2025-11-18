# Write a program that prints numbers from 1 to 100
# multiples of 3 print "Fizz"
# multiples of 5 print "Buzz"
# multiples of both 3 and 5 print "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)