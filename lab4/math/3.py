import cmath 
n = int(input("The number of sides: "))
l = int(input("The length of a side: "))
Area = n * (l**2)/4 * cmath.tan(cmath.pi/n)
print (f"Area is equal to: {Area}")