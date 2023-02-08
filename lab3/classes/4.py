class point:
    def show (self,x,y):
        self.x = x
        self.y = y 
        print(x,y)
    def move (self,x,y,x2,y2):
        self.x2 = x + x2 
        self.y2 = y + y2  
        print(x2,y2)
    def dist(self,x,y,x2,y2):
        distance = ((x2-x)**2 + (y2-y)**2)**0.5
        print (distance)
x , y =map(int,input().split())
x2 , y2 =map(int,input().split())
lab3 = point()
lab3.show(x,y)
lab3.move(x,y,x2,y2)
lab3.dist(x,y,x2,y2)


