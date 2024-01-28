#Câu 1:
class Employee():
    def __init__ (self, name, position):
        self.name = name
        self.position = position
    def say_hi(self):
        print(f"Hi, my name is {self.name}.")
    def tell_position(self):
        print(f"I am a {self.position}.")
# driver code
ten = Employee("Hieu", "Teaching Executive")
ten.say_hi()
ten.tell_position()

# Câu 2:
# Tạo class của hình chữ nhật
class Rectangle:
    def __init__(self, height, width):
        self.height =height
        self.width = width
    def caculate_perimeter(self):
        return(self.height + self.width) * 2
    def caculater_area(self):
        return self.height * self.width
# Tạo class của hình tròn
class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius
    def caculate_perimeter(self):
        return 2*self.PI * self.radius
    def caculater_area(self):
        return self.PI * self.radius**2
# driver code
# get shape
print("Shape (rectangle|circle): ", end = "")
shape_name = input()

# get coresponding shape sizes
shape = None
if shape_name == "rectangle":
    print("Height: ", end="")
    height = float(input())
    print("Width: ", end="")
    width = float(input())
    shape = Rectangle(height, width)
elif shape_name == "circle":
    print ("Radius: ", end="")
    radius = float(input())
    shape = Circle(radius)
else:
    print("\n=> Invalid")

if shape != None:
    print()
    print("=> Perometer: ", shape.caculate_perimeter())
    print("=> Area: ", shape.caculater_area())