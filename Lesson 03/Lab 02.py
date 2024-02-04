# Câu 1
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def __str__(self):
        return f"Rectangle object with heigth= {self.height} anh width = {self.width}"
rect = Rectangle(2,1)
print(rect)

# Câu 2
class MathList:
    def __init__(self, values):
        self.values = values
        self.length = len(values)

    def __str__(self):
        return str(self.values)

    def __add__(self, value):
        for i in range (self.length):
            self.values[i] += value
        return self
    
    def __sub__(self, value):
        for i in range (self.length):
            self.values[i] -= value
        return self
    
my_list = MathList([1,2,3,4,5])
print(my_list)

my_list += 2
print(my_list)