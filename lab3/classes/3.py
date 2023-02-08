class Shape:
    def area(self):
        print(0)
class Rect(Shape) :
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    def areas(self):
        print(self.length*self.width)

a = int(input())
b = int(input())
Area = Rect(a,b)
Area.areas()
