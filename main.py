from asyncio.windows_events import NULL
from pickle import FALSE, TRUE
import turtle as t
import random
import time
import data as d
import categories as c
import Interface as inf

#initiate turtle
window=t.Screen()
t.bgcolor("black")
t.setup(1080,720)




#FUNCTIONS

#It uses the class to make the figure and the x and y position of the figure can be change
def createGrid(x,y,whatlist):
    for i in range(3):
        y1 = y-50*i
        for j in range(3):
            x1 = x+50*j
            isFill = whatlist[i][j]
            figure=d.box(x1,y1,isFill)
            figure.creatBox()

# this for randomizing the choices    

def randomchoices():
    choiceorderlist = []
    while True:
        randomchoice = random.randint(1,4)

        while randomchoice not in choiceorderlist:
            choiceorderlist.append(randomchoice)
        if len(choiceorderlist)==4:
            break
    return choiceorderlist

# To rotate the choices and to have extr challenge
# The rotation is random
def rotate(listname, choice):
    for r in rotations[random.randint(0,3)]:
        listname.append(choice[1][r])
    listname = [listname[0:3],listname[3:6],listname[6:9]]
    return listname


#This code is timer for the user to answer
def gameTimer(tm):
    for i in range(tm):

        time.sleep(1)
        t.clear()
        t.hideturtle()
        t.color("white")
        t.speed(100)
        t.write(tm-i, move=False, align="left", font=("Arial", 30, "bold"))
    time.sleep(1)
    t.clear()
    t.write(0, move=False, align="left", font=("Arial", 30, "bold"))
    return TRUE


#This determine if the answer is correct
def checker(a,b):
    if a==b:
        return 1
    else:
        return 0





#MAIN GAME

#The variables the level increment every round and the score if the answer is correct

score=0

level = 0

# this code it to write a letter in turte
# This is used to write the score
displayscore = t.Turtle()
displayscore.hideturtle()
displayscore.goto(-500,300)
displayscore.color("white")
displayscore.speed(100)
displayscore.write("level: 1  score: 0", move=False, align="left", font=("Arial", 20, "bold"))

#This loop is to proceed to the next level, the level to increase every round
while (level <= 11):

#Show the level in console
    print("level: ",level+1)

#Access the categories form categories.py
    category = c.catlist[level]

# This code is for creating the figure

    figure = category[0]


#Randomizing the choices and assigning it in every figure
    order = randomchoices()
    correctchoice = order.index(1)+1
    choice1 = category[order[0]]
    choice2 = category[order[1]]
    choice3 = category[order[2]]
    choice4 = category[order[3]]


#to print the correct choicec in coonsole this code is not necessary
    print("correct choice: ", correctchoice)


#This code is for manipulating the list of each category for it to use for the class that create the figure
    figurelist = []
    c1list = []
    c2list = []
    c3list = []
    c4list = []



    for r in d.r0:
        figurelist.append(figure[r])
        
    rotations = [d.r0,d.r1,d.r2,d.r3]

    figurelist = [figurelist[0:3],figurelist[3:6],figurelist[6:9]]



# The figure is created including the choices
    createGrid(-75,310,figurelist)

    createGrid(-450,-50,rotate(c1list,choice1))

    createGrid(-200,-50,rotate(c2list,choice2))

    createGrid(50,-50,rotate(c3list,choice3))

    createGrid(300,-50,rotate(c4list,choice4))

#Accept data from user where it clicked
    t.onscreenclick(inf.clickCoor)

#timer starts
    countdown = gameTimer(5)
    if countdown==TRUE:
        print("TIMES UP")


#use interface module to determine which choise is chosed
    inf.ccvalue


#Determine if the choosed is equal to the correct answer
    score = score + checker(correctchoice, inf.ccvalue)



#print score in the console
    print("score: ", score)


#clearing the screen
    window.resetscreen()
    level +=1

#showing the score
    writescore = "Level: "+str(level+1)+" "+"score: "+str(score)

    displayscore.clear()
    displayscore.hideturtle()
    displayscore.goto(-500,300)
    displayscore.color("white")
    displayscore.speed(100)
    displayscore.write(writescore, move=False, align="left", font=("Arial", 20, "bold"))




window.mainloop()