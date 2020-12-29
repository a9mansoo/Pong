import turtle
from paddle import Paddle

player_1 = 1
player_2 = 2

# Create a window, turtle module will load a screen for us
window = turtle.Screen()

window.title("Extreme ping pong")

window.bgcolor("pink")

# Controls the size of the screen on start-up
window.setup(width=800, height=600) 

#stops window from updating and manually update the window for
# speeded up game
window.tracer(0)

#Score
score_a = 0
score_b = 0


# left paddle
paddle_left = Paddle(player_1)
#paddle_left = turtle.Turtle()
#speed of animation, sets to maximum possible speed
#paddle_left.speed(0)
#paddle_left.shape("square")
#paddle_left.color("purple")
#paddle_left.shapesize(stretch_wid=5, stretch_len=1)
#dont draw line
#paddle_left.penup()
#paddle_left.goto(-350,0)

# Paddle b, right paddle
paddle_right = Paddle(player_2)
'''
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("purple")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)
'''
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal")) 


# Function
'''
def paddle_left_up():
    # know the current y coordinate
    y = paddle_left.ycor()
    # add 20 pixels to y
    y += 20
    # now set the new coordinate
    paddle_left.sety(y)

def paddle_left_down():
    # know the current y coordinate
    y = paddle_left.ycor()
    # add 20 pixels to y
    y -= 20
    # now set the new coordinate
    paddle_left.sety(y)

def paddle_right_up():
    # know the current y coordinate
    y = paddle_right.ycor()
    # add 20 pixels to y
    y += 20
    # now set the new coordinate
    paddle_right.sety(y)

def paddle_right_down():
    # know the current y coordinate
    y = paddle_right.ycor()
    # add 20 pixels to y
    y -= 20
    # now set the new coordinate
    paddle_right.sety(y)
    
'''    
# Keyboard binding
# listen to keyboard input
window.listen()
window.onkeypress(paddle_left.paddle_up(), "w")
window.onkeypress(paddle_left.paddle_down(), "s")
window.onkeypress(paddle_right.paddle_up(), "Up")
window.onkeypress(paddle_right.paddle_down(), "Down")

# Main game loop, actual start of game
while True:
    # update the screen
    window.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    # top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        #reverse the direction
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        #reverse the direction
        ball.dy *= -1   
    #left and right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        #reverse the direction
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 
    if ball.xcor() < -390:
        ball.goto(0, 0)
        #reverse the direction
        ball.dx *= -1    
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle collision with ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.get_ycor() + 40) and (ball.ycor() > paddle_right.get_ycor() - 40):
        ball.setx(340)
        ball.dx *=-1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.get_ycor() + 40) and (ball.ycor() > paddle_left.get_ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1    
