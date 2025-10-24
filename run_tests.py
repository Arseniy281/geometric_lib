
import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

def rectangle_area(a, b):
    return a * b

def rectangle_perimeter(a, b):
    return 2 * (a + b)

def square_area(a):
    return a * a

def square_perimeter(a):
    return 4 * a

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c