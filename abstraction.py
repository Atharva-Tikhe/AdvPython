from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        print("Radius of the circle: ", 4)

    def area(self):
        circle_area = 3.14*radius**2
        print("Area of the circle: ", circle_area)
 
    def perimeter(self):
        circle_perimeter = 2*3.14*radius
        print("Perimeter of the circle: ", circle_perimeter)



class Square(Shape):
    def __init__(self, side):
        self.side = side
        print("Side of the square: ", 4)


    def area(self):
        square_area = side**2
        print("Area of the square: ", square_area)


    def perimeter(self):
        square_perimeter = side*4
        print("Perimeter of the square: ", square_perimeter)


while True:
    print("\nMain Menu")
    print("1. Calculate Area")
    print("2. Calculate Perimeter")
    print("3. Continue?")
    choice1 = int(input("Enter the Choice: "))

    if choice1 == 1:
        print("\nCalculate Area")
        print("1. Circle")
        print("2. Square")
        choice2 = int(input("Enter the Choice:"))

        if choice2 == 1:
            radius = int(input("Enter Radius of the Circle:"))
            c=Circle(radius)
            c.area()

        elif choice2 == 2:
            side = int(input("Enter the side of the square:"))
            s=Square(side)
            s.area()

            
    elif choice1 == 2:
        print("\nCalculate Perimeter")
        print("1. Circle")
        print("2. Square")
        choice2 = int(input("Enter the Choice:"))

        if choice2 ==1:
            radius = int(input("Enter Radius of the Circle: "))
            c1 = Circle(radius)
            c1.perimeter()
    
        elif choice2 ==2:
            side = int(input("Enter the side of the Square: "))
            s1 = Square(side)
            s1.perimeter()
