import turtle

'''
Scoreboard class
 should be used by the Ball Class
'''

class ScoreBoard():
    # variables here are class specific so kinda like static variables
    def __init__(self):
        self.scoreboard = turtle.Turtle()
        self.scoreboard.speed(0)
        self.scoreboard.color("black")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 260)
        self.player_1 = "Player A"
        self.player_2 = "Player B"
        self.player_1_score = 0
        self.player_2_score =0

    def print_board(self):
        self.scoreboard.write("{} {}  {} {}".format(self.player_1, self.player_1_score,
                                                    self.player_2, self.player_2_score),
                              align="center", font=("Courier", 24, "normal"))
        


    def increment_score(self, player_name):
        if player_name == self.player_1:
            self.player_1_score += 1
        elif player_name == self.player_2:
            self.player_2_score += 1

        self.scoreboard.clear()
        
        
        
