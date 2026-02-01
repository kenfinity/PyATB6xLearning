pb_public_b = 12

def my_function():
    pb_a  = 10
    print(pb_a)
    pb_public_b = 5
    print(pb_public_b)

# cannot call a function that is defined inside another function

print(pb_public_b)
my_function()