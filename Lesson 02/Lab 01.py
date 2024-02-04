# Câu 1:
class Employee:
    def __init__(self, name, position):
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
        self.height = height
        self.width = width

    def caculate_perimeter(self):
        return (self.height + self.width) * 2

    def caculater_area(self):
        return self.height * self.width


# Tạo class của hình tròn
class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def caculate_perimeter(self):
        return 2 * self.PI * self.radius

    def caculater_area(self):
        return self.PI * self.radius**2


# driver code
# get shape
print("Shape (rectangle|circle): ", end="")
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
    print("Radius: ", end="")
    radius = float(input())
    shape = Circle(radius)
else:
    print("\n=> Invalid")

if shape != None:
    print()
    print("=> Perometer: ", shape.caculate_perimeter())
    print("=> Area: ", shape.caculater_area())

# Câu 3
from datetime import datetime


class CustomDate:
    def __init__(self):
        self.time = datetime.now()

    def get_date(self):
        return self.time.strftime("%d/%m/%y")

    # return f"{self.time.day:02d}/{self.month:02d}/{self.time.year:04d}"
    # datetime_object.strftime(format): là một phương thức được sd để đđịnh dạn chuổi từ một đối tương thời gian (datetime). Viết tắt của từ "string format time <=> định dạng thời gian thành chuổi"

    def get_time(self):
        return self.time.strftime("%H:%M:%S")

    # return f"{self.time.hour:02d}/{self.minute:02d}/{self.time.second:02d}"


# driver code
now = CustomDate()
print(now.get_date())
print(now.get_time())


# Câu 4
class DateHandler:
    def __init__(self) -> None:
        pass

    @classmethod  # là một decorator.
    # Decorator là một cú pháp ngắn gọn trong Python để thay đổi hoặc mở rộng hành vi của một hàm hoặc phương thức.
    def format_date(cls, time):
        return time.strftime("%d/%m/%y")

    @classmethod
    def get_day_between(cls, time_start, time_end):
        return (time_end - time_start).days


from datetime import datetime

start_date = datetime(1999, 4, 25)
end_date = datetime(2000, 4, 25)

print("Start: ", DateHandler.format_date(start_date))
print("End: ", DateHandler.format_date(end_date))
print("Days between: ", DateHandler.get_day_between(start_date, end_date))
