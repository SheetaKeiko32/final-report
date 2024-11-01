
import turtle
import random
# from tkinter import canvas
class Mainchara:
    def __init__(self):
        
        self.Mainchara=turtle.Turtle()
        self.Mainchara.speed(0)
        window.addshape(r'/Users/mac/Desktop/final-report/mainchara.gif')
        self.Mainchara.shape(r'/Users/mac/Desktop/final-report/mainchara.gif')
        self.Mainchara.penup()
        self.Mainchara.goto(-0,-300)

    def trai(self):
        x = self.Mainchara.xcor()
        x -= 20
        if x < -280:
            x = -280
        self.Mainchara.setx(x)

    def phai(self):                        
        x = self.Mainchara.xcor()
        x += 20
        if x > 280:
            x = 280
        self.Mainchara.setx(x)        

class Laser:
    def __init__(self):
        self.Laser=turtle.Turtle()
        window.addshape(r'/Users/mac/Desktop/final-report/laser  .gif')
        self.Laser.speed(0)
        self.Laser.shape(r'/Users/mac/Desktop/final-report/laser  .gif')
        self.Laser.goto(0,-210)
        self.Laser.hideturtle()
        self.Laser_state='ready'


    def laser(self,Mainchara):
        if self.Laser_state == "ready":
            self.Laser_state = "fire"
            self.Laser.goto(Mainchara.turtle.xcor(), Mainchara.turtle.ycor() )
            self.Laser.showturtle()
        
    def reset(self):
        self.Laser.hideturtle()
        self.Laser.goto(0, -210)
        self.Laser_state = "ready"
 

class Alien:
    def __init__(self):

        self.Aliens = []
        for _ in range(5):
            Alien=turtle.Turtle()
            Alien.speed(0)
            window.addshape(r'/Users/mac/Desktop/final-report/e2 .gif')
            Alien.shape(r'/Users/mac/Desktop/final-report/e2 .gif')
            Alien.penup()
            Alien.goto(random.randint(-300, 300), random.randint(100, 250))
            self.Aliens.append(Alien)   


def check_collision(laser, alien):
    return laser.Laser.distance(alien) < 20


pass

window = turtle.Screen()
window.bgpic(r'/Users/mac/Desktop/final-report/bg (2).gif')
window.title('robot')
window.bgcolor('black')
window.setup(width=800, height=1000)

window.listen()
window.onkeypress(Mainchara.trai,'a')
window.onkeypress(Mainchara.phai,'d')
window.onkeypress(Laser.laser,'space')

while True:
    window.update()
    

    for alien in alien.aliens:
        alien.sety(alien.ycor()-6)
        if alien.ycor() < -300:
            alien.goto(random.randint(-300, 300), random.randint(100, 250))
        if check_collision(alien,laser) < 20:
            Laser.reset()
 


            


    if Laser_state == 'fire':
        Laser.sety(Laser.ycor() )

    if Laser.ycor() > 300:
        Laser.hideturtle()
        Laser_state = "ready"

window.mainloop()




# import turtle
# import random

# class Mainchara:
#     def __init__(self):
#         self.Mainchara = turtle.Turtle()
#         self.Mainchara.speed(0)
#         window.addshape(r'/Users/msv/Documents/GitHub/final-report/mainchara.gif')
#         self.Mainchara.shape(r'/Users/msv/Documents/GitHub/final-report/mainchara.gif')
#         self.Mainchara.penup()
#         self.Mainchara.goto(0, -300)

#     def trai(self):
#         x = self.Mainchara.xcor()
#         x -= 20
#         if x < -290:
#             x = -290
#         self.Mainchara.setx(x)

#     def phai(self):                        
#         x = self.Mainchara.xcor()
#         x += 20
#         if x > 290:
#             x = 290
#         self.Mainchara.setx(x)        

# class Laser:
#     def __init__(self):
#         self.Laser = turtle.Turtle()
#         window.addshape(r'/Users/mac/Desktop/final-report/bg (2).gif')
#         self.Laser.speed(0)
#         self.Laser.shape(r'/Users/mac/Desktop/final-report/bg (2).gif')
#         self.Laser.penup()
#         self.Laser.goto(0, -210)
#         self.Laser.hideturtle()
#         self.Laser_state = 'ready'

#     def fire(self, mainchara):
#         if self.Laser_state == "ready":
#             self.Laser_state = "fire"
#             self.Laser.goto(mainchara.Mainchara.xcor(), mainchara.Mainchara.ycor() + 20)
#             self.Laser.showturtle()

#     def reset(self):
#         self.Laser.hideturtle()
#         self.Laser.goto(0, -210)
#         self.Laser_state = "ready"

# class Alien:
#     def __init__(self):
#         self.aliens = []
#         for _ in range(5):
#             alien = turtle.Turtle()
#             alien.speed(0)
#             window.addshape(r'/Users/mac/Desktop/final-report/e1 .gif')
#             alien.shape(r'/Users/mac/Desktop/final-report/e1 .gif')
#             alien.penup()
#             alien.goto(random.randint(-300, 300), random.randint(100, 250))
#             self.aliens.append(alien)

# # Function for collision detection
# # def collision(laser, alien):
# #     return laser.Laser.distance(alien) < 20

# # Set up the screen
# window = turtle.Screen()
# window.bgpic(r'/Users/msv/Documents/GitHub/final-report/bg (2).gif')
# window.title('robot')
# window.bgcolor('black')
# window.setup(width=800, height=1000)

# # Create instances
# mainchara = Mainchara()
# laser = Laser()
# alien_group = Alien()

# # Keyboard bindings
# window.listen()
# window.onkeypress(mainchara.trai, 'a')
# window.onkeypress(mainchara.phai, 'd')

# def fire_laser():
#     laser.fire(mainchara)

# window.onkeypress(fire_laser, 'space')

# while True:
#     window.update()
    
#     for alien in alien_group.aliens:
#         alien.sety(alien.ycor() - 2)

#         if alien.ycor() < -300:
#             alien.goto(random.randint(-300, 300), random.randint(100, 250))
        
#         # if collision(laser, alien):
#         if laser.Laser.distance(alien) < 20:
#             laser.reset()
#             alien.goto(random.randint(-300, 300), random.randint(100, 250))    

#     if laser.Laser_state == 'fire':
#         laser.Laser.sety(laser.Laser.ycor() + 40)

#     if laser.Laser.ycor() > 300:
#         laser.reset()

# window.mainloop()


