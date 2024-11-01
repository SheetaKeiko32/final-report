import turtle
import random

def run_game():
    class Mainchara:
        def __init__(self):
            self.Mainchara = turtle.Turtle()
            self.Mainchara.speed(0)
            window.addshape(r'C:\Users\Admin\Desktop\final-report\mainchara.gif')
            self.Mainchara.shape(r'C:\Users\Admin\Desktop\final-report\mainchara.gif')
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

        def hide(self):
            self.Mainchara.hideturtle()

    class Laser:
        def __init__(self):
            self.Laser = turtle.Turtle()
            window.addshape(r'C:\Users\Admin\Desktop\final-report\laser  .gif')
            self.Laser.speed(0)
            self.Laser.shape(r'C:\Users\Admin\Desktop\final-report\laser  .gif')
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

    class Scoreboard:
        def __init__(self):
            self.score = 0
            self.score_board = turtle.Turtle()
            self.score_board.speed(0)
            self.score_board.color('white')
            self.score_board.penup()
            self.score_board.goto(0, 250)
            self.score_board.hideturtle()
            self.update_score()

        def update_score(self):
            self.score_board.clear()  
            self.score_board.write(f'Score: {self.score}', align='center', font=('Courier', 24, 'normal')) 
        
        def increment_score(self):
            self.score += 10
            self.update_score()
        
        def losing(self):
            self.score_board.clear()
            self.score_board.write(f'Final Score: {self.score}', align='center', font=('Courier', 50, 'normal'))
        
        def displaymessagewhenturn200(self):
            self.scoreboard.write(f'Enemy now need 2 hits to die', align='center')

        def clearmessage(self):
            message.clear()
            



    class Alien:
        def __init__(self):
            self.aliens = []
            for _ in range(5):
                alien = turtle.Turtle()
                alien.speed(0)
                window.addshape(r'C:\Users\Admin\Desktop\final-report\e1 .gif')
                alien.shape(r'C:\Users\Admin\Desktop\final-report\e1 .gif')
                alien.penup()
                alien.goto(random.randint(-300, 300), random.randint(100, 250))
                alien.hits = 0
                self.aliens.append(alien)

        def hide(self):
            for alien in self.aliens:
                alien.hideturtle()

    window = turtle.Screen()
    window.bgpic(r'C:\Users\Admin\Desktop\final-report\bg (2).gif')
    window.title('robot')
    window.bgcolor('black')
    window.setup(width=800, height=800)

    mainchara = Mainchara() 
    laser = Laser()
    alien_group = Alien()
    scoreboard = Scoreboard()

    hit_message_turtle = turtle.Turtle()
    hit_message_turtle.speed(0)
    hit_message_turtle.color('yellow')
    hit_message_turtle.penup()
    hit_message_turtle.hideturtle()

    window.listen()
    window.onkeypress(mainchara.trai, 'a')
    window.onkeypress(mainchara.phai, 'd')

    def fire_laser():
        laser.fire(mainchara)

    window.onkeypress(fire_laser, 'space')

    while True:
        window.update()
        
        for alien in alien_group.aliens:
            alien.sety(alien.ycor() - 3)

            if alien.ycor() < -300:
                alien_group.hide()
                mainchara.hide()
                scoreboard.losing()
            
            if mainchara.Mainchara.distance(alien) < 20:
                alien_group.hide()
                mainchara.hide()
                scoreboard.losing()
        


            # Check for hit
            if laser.Laser.distance(alien) < 20 and laser.Laser_state == 'fire':
                laser.reset()
                alien.hits += 1  # Increment hits


        
                if scoreboard.score >= 50:
                    if alien.hits >= 2:  # Require 2 hits if score >= 200
                        hit_message_turtle.goto(0, 200)
                        hit_message_turtle.write('Enemies now need 2 hits to die', align='center', font=('Courier', 18,'normal'))
                        window.ontimer(hit_message_turtle.clear, 3000) 
                        hit_message_turtle.hideturtle()
                        alien.goto(random.randint(-300, 300), random.randint(100, 250))
                        alien.hits = 0  # Reset hits
                        scoreboard.increment_score()  # Increment score
                else:
                    alien.goto(random.randint(-300, 300), random.randint(100, 250))    
                    alien.hits = 0  # Reset hits
                    scoreboard.increment_score()  # Increment score
    
        if laser.Laser_state == 'fire':
            laser.Laser.sety(laser.Laser.ycor() + 40)

        if laser.Laser.ycor() > 300:
            laser.reset()
