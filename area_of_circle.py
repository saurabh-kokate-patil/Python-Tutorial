import math

def area_of_circle(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    area = area_of_circle(r)
    print(f"Area of the circle with radius {r} is {area:.2f}")