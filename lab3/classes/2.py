class Shape() : 
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self,length) :
        self.length=length
    def areas(self) :
        n = pow(self.length,2)
        print(n)

a = int(input())
Area = Square(a)
Area.areas()

