import turtle
'''
Paddle class

'''

class Paddle:
    #x_position = 0
    #y_position = 0
    player_num = 0
    paddle = None

    def __init__(self, player_num):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("purple")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        #dont draw line
        self.paddle.penup()
        if player_num == 1:
            self.paddle.goto(-350,0)
        else:
            self.paddle.goto(350,0)
        self.player_num = player_num

    def paddle_up(self):
        y_position = self.paddle.ycor()
        y_position += 20
        self.paddle.sety(y_position)

    def paddle_down(self):
        y_position = self.paddle.ycor()
        y_position -= 20
        self.paddle.sety(y_position)

    def get_ycor(self):
        return self.paddle.ycor()
        
    
        
        
        
        
