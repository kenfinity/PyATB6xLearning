# Q - Create a function which will take a positive number from the user and perform square of the number?
# i/o = 3
# o/p = 9

def square_num(num):
    if num >= 0:
        return num * num
    else:
        return "not a valid number"

result =  square_num(6)
print(result)


# Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

def triangle_type(side1, side2, side3):
    if side1 == side2 and side1 != side3 or side2 == side3 and side2!= side1 or side3 == side1 and side3 != side2:
        print("The triangle is isoceles")
    elif side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 != side2 and side2 != side3 and side1 != side3:
        print("The triangle is scalene")

triangle_type(1, 2, 3)
triangle_type(1, 3, 2)
triangle_type(2, 3, 1)
triangle_type(2, 1, 3)
triangle_type(3, 2, 1)
triangle_type(3, 1, 2)

triangle_type(3, 2, 3)

triangle_type(3, 3, 3)
