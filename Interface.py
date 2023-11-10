import turtle as t


# This code is to accept data from user to determine the choices selected

ccvalue = 0
def clickCoor(x,y):
    
    global ccvalue
    choosed = 0
    if -200<=y<=-50:
        if -450<=x<=-300:
            choosed = 1

        if -200<=x<=-50:
            choosed = 2
        
        if 50<=x<=200:
            choosed = 3

        if 300<=x<=450:
            choosed = 4
        else:
            pass
    else:
        pass

    ccvalue = choosed

    return choosed




# this code is not used

class button(t.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        # self.x2=x2
        self.y=y
        # self.y2=y2
    def createbutton(self):
        self.speed(100)
        self.hideturtle()
        self.color("blue")
        self.fillcolor("white")
        self.penup()
        self.goto(self.x,self.y)
        self.pendown()
        self.setheading(0)
        for i in range(4):
            self.pencolor("grey")
            self.forward(160)
            self.right(90)



