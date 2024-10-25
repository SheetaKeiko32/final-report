
import turtle
import random

class Mainchara:
    def __init__(self):
        self.Mainchara = turtle.Turtle()
        self.Mainchara.speed(0)
        window.addshape(r'/Users/mac/Desktop/final-report/mainchara.gif')
        self.Mainchara.shape(r'/Users/mac/Desktop/final-report/mainchara.gif')
        self.Mainchara.penup()
        self.Mainchara.goto(0, -300)

    def trai(self):
        x = self.Mainchara.xcor()
        x -= 20
        if x < -290:
            x = -290
        self.Mainchara.setx(x)

    def phai(self):                        
        x = self.Mainchara.xcor()
        x += 20
        if x > 290:
            x = 290
        self.Mainchara.setx(x)        

class Laser:
    def __init__(self):
        self.Laser = turtle.Turtle()
        window.addshape(r'/Users/mac/Desktop/final-report/laser  .gif')
        self.Laser.speed(0)
        self.Laser.shape(r'/Users/mac/Desktop/final-report/laser  .gif')
        self.Laser.penup()
        self.Laser.goto(0, -210)
        self.Laser.hideturtle()
        self.Laser_state = 'ready'

    def fire(self, mainchara):
        if self.Laser_state == "ready":
            self.Laser_state = "fire"
            self.Laser.goto(mainchara.Mainchara.xcor(), mainchara.Mainchara.ycor() + 20)
            self.Laser.showturtle()

    def reset(self):
        self.Laser.hideturtle()
        self.Laser.goto(0, -210)
        self.Laser_state = "ready"

class Alien:
    def __init__(self):
        self.aliens = []
        for _ in range(10):
            alien = turtle.Turtle()
            alien.speed(0)
            window.addshape(r'/Users/mac/Desktop/final-report/e2 .gif')
            alien.shape(r'/Users/mac/Desktop/final-report/e2 .gif')
            alien.penup()
            alien.goto(random.randint(-300, 300), random.randint(100, 250))
            self.aliens.append(alien)

window = turtle.Screen()
window.bgpic(r'/Users/mac/Desktop/final-report/bg (2).gif')
window.title('robot')
window.bgcolor('black')
window.setup(width=800, height=1000)


mainchara = Mainchara()
laser = Laser()
alien_group = Alien()


window.listen()
window.onkeypress(mainchara.trai, 'a')
window.onkeypress(mainchara.phai, 'd')

def fire_laser():
    laser.fire(mainchara)

window.onkeypress(fire_laser, 'space')

while True:
    window.update()
    
    for alien in alien_group.aliens:
        alien.sety(alien.ycor() - 2)

        if alien.ycor() < -300:
            alien.goto(random.randint(-300, 300), random.randint(100, 250))
        

        if laser.Laser.distance(alien) < 20:
            laser.reset()
            alien.goto(random.randint(-300, 300), random.randint(100, 250))    

    if laser.Laser_state == 'fire':
        laser.Laser.sety(laser.Laser.ycor() + 40)

    if laser.Laser.ycor() > 300:
        laser.reset()

window.mainloop()


