import turtle
import random
import time
'''
Mod class

'''

class Mod:
    def __init__(self):
        # also can we maybe inherit from the Turtle module?
        # or is the dependency okay?
        # list of power ups and power downs that can be generated
        self.powers = ["Points", "Speed-up", "Speed-down"]
        self.current_item = None
        self.graphic = turtle.Turtle()

    def generate_modification(self):
        item_index = 0
        #item_index = random.randint(0, len(self.powers) - 1)
        power = self.powers[item_index]

        if power == "Points":
            for i in range(5):
                self.graphic.forward(100)
                time.sleep(5)
                self.graphic.right(144)

        elif power == "Speed-up":
            pass

        else:
            #draw speed-down shape
            pass



    def clear_power(self):
        self.graphic.clear()

    def is_power_taken(self, ball, player, scoreboard):
        # determines which player hit the power up/down and
        # carries out the appropriate fixation (adding points, speed)
        # we need to check if the ball came into contact with the graphic
        # and then we need to apply the power
        pass
            

        
    
        
        
        
        
