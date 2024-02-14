# Author
# Date
# Description : Memory Game with Turtle
# Revision History
# Name      Date       Desc
# scl        2/12/24   Initial code base 
import random
import turtle
import time

start_pos_x = -100
start_pos_y = 0
level = 3

offset = 100

def drawSquare(x, y):
    turle.down()
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)





for x in range(level):
    #data type is interger
    a = random.randint(1,99)

    # data structure
    "number_list".append(a)
    turtle.write(str(a), font=("Verdana",20, "normal"))
    turtle.up()
    save_pos = (x * offset, 0)
    turtle.goto(save_pos)

    drawSquare(x * offset, 0)
    turtle.goto(save_pos)
    time.sleep(3)

turtle.clear()


# please enter the answers
for x in range(level):
 answer = int(input("The numbers were "))
                

    

    
  




