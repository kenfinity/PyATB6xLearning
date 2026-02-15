# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1 = int(input("enter the side1: "))
side2 = int(input("enter the side2: "))
side3 = int(input("enter the side3: "))

def check_triangle(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a == b == c:
                return "triangle is equilateral"
            elif a == b or a == c or b == c:
                return "triangle is isosceles"
            else:
                return "triangle is scalene"
        else:
            print("not a triangle")
    else:
        print("not a valid length")



result = check_triangle(side1,side2,side3)
print(f"The triangle is classified as: {result}")

