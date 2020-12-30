import turtle
from scoreboard import ScoreBoard 

'''
Ball class

'''

class Ball():

    def __init__(self):
        self.ball = turtle.Turtle()
        self.sb = ScoreBoard()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx = 0.3
        self.ball.dy = 0.3
        self.sb.print_board()

    def go_ball(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def check_ball(self):
        # Top and bottom
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            #reverse the direction
            self.ball.dy *= -1
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            #reverse the direction
            self.ball.dy *= -1   

        # Left and right
        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            #reverse the direction
            self.ball.dx *= -1
            self.sb.increment_score("Player A")
            self.sb.print_board()
            
        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            #reverse the direction
            self.ball.dx *= -1
            self.sb.increment_score("Player B")
            self.sb.print_board()

    def check_paddle(self, paddle_right, paddle_left):
        # Check collision with paddle
        if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (self.ball.ycor() < paddle_right.get_ycor() + 40) and (self.ball.ycor() > paddle_right.get_ycor() - 40):
            self.ball.setx(340)
            self.ball.dx *=-1
        if (self.ball.xcor() < -340 and self.ball.xcor() > -350) and (self.ball.ycor() < paddle_left.get_ycor() + 40) and (self.ball.ycor() > paddle_left.get_ycor() - 40):
            self.ball.setx(-340)
            self.ball.dx *=-1


        
