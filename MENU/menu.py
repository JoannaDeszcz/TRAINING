import math

def area_square(a):
    return a * a

def area_rectangle(a, b):
    return a * b

def area_circle(r):
    return math.pi * r ** 2

def area_triangle(a, h):
    return 0.5 * a * h

def area_trapezoid(a, b, h):
    return (a + b) / 2 * h

while (True):   
    choice = int(input("""

    MENU 

    Select the figure whose area you want to calculate:
    1. square
    2. rectangle
    3. circle
    4. triangle
    5. trapezoid

    Figure: """))

    if (choice == 1):
        a = float(input("Specify side of square: "))
        if(a>0):
            print("The area of the square is:", area_square(a))
        else:
            print("Cannot perform the action. The length of the side must be a positive number. Try again ") 
    elif (choice == 2):
        a = float(input("Specify the first side of the rectangle: "))
        b = float(input("Enter the second side of the rectangle: "))
        if(a,b>0):
            print("The area of the rectangle is:", area_rectangle(a,b))
        else:
            print("Cannot perform the action. The length of the side must be a positive number. Try again ") 
    elif (choice == 3):
        r = float(input("Specify radius of circle: "))
        if(r>0):
            print("The area of the circle is:", area_circle(r))
        else:
            print("Cannot perform the action. The length of the radius must be a positive number. Try again ")
    elif (choice == 4):
        a = float(input("Specify side of triangle: "))
        h = float(input("Enter the height of the triangle: "))
        if(a,h>0):
            print("The area of the triangle is:", area_triangle(a,h))
        else:
            print("Cannot perform the action. Side length and height must be positive numbers. Try again ")
    elif (choice == 5):
        a = float(input("Specify the first side of the rectangle: "))
        b = float(input("Enter the second side of the rectangle: "))
        h = float(input("Enter height of trapezoid: "))    
        if(a,b,h>0):
            print("The area of the trapezoid is:", (a,b,h))
        else:
            print("Cannot perform the action. The lengths of the side and the height must be positive numbers. Try again ")