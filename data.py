import turtle as t

#If the figure is rotated the sequence of grid  is the following
#the number next to r in variable name is the degree of rotation multiply by 90 degree.

r0 = [0,1,2,3,4,5,6,7,8]
r1 = [2,5,8,1,4,7,0,3,6]
r2 = [8,7,6,5,4,3,2,1,0]
r3 = [6,3,0,7,4,1,8,5,2]



#This is the class for each figure including the choices it uses turtle to create the figure
#Class is used to make multiple figure in one code

class box(t.Turtle):
    def __init__(self,x,y,isfill):
        super().__init__()
        self.x=x
        self.y=y
        self.isfill=isfill
    def creatBox(self):
        self.speed(1000)
        self.hideturtle()
        self.color("white")
        self.fillcolor("white")
        self.penup()
        self.goto(self.x,self.y)
        self.pendown()
        self.setheading(0)
        if self.isfill == 1:
            self.begin_fill()
            for i in range(4):
                self.forward(50)
                self.right(90)
            self.end_fill()
        else:
             for i in range(4):
                self.pencolor("grey")
                self.forward(50)
                self.right(90)






