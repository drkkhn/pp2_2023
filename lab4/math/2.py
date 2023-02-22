height = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
def area(h,a,b) :
    Area = ((a+b)/2)*h 
    print(f"Area of trapezoid: {Area}")
area(height,a,b)
