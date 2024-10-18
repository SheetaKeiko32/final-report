# import turtle
# import random

# # Setup the screen
# wn = turtle.Screen()
# wn.title("Alien Drop")
# wn.bgcolor("black")
# wn.setup(width=600, height=600)

# # Player
# player = turtle.Turtle()
# player.speed(0)
# player.shape("square")
# player.color("green")
# player.penup()
# player.goto(0, -250)
# player.shapesize(stretch_wid=1, stretch_len=3)

# # Bullet
# bullet = turtle.Turtle()
# bullet.speed(0)
# bullet.shape("triangle")
# bullet.color("red")
# bullet.penup()
# bullet.hideturtle()
# bullet.goto(0, -240)
# bullet.setheading(90)
# bullet_state = "ready"
 
# # Aliens
# aliens = []
# for _ in range(5):
#     alien = turtle.Turtle()
#     alien.speed(0)
#     alien.shape("circle")
#     alien.color("orange")
#     alien.penup()
#     alien.goto(random.randint(-290, 290), random.randint(100, 250))
#     aliens.append(alien)

# # Functions
# def move_left():
#     x = player.xcor()
#     x -= 20
#     if x < -280:
#         x = -280
#     player.setx(x)

# def move_right():
#     x = player.xcor()
#     x += 20
#     if x > 280:
#         x = 280
#     player.setx(x)

# def fire_bullet():
#     global bullet_state
#     if bullet_state == "ready":
#         bullet_state = "fire"
#         bullet.goto(player.xcor(), player.ycor() + 10)
#         bullet.showturtle()

# def is_collision(t1, t2):
#     return t1.distance(t2) < 20

# # Keyboard bindings
# wn.listen()
# wn.onkeypress(move_left, "Left")
# wn.onkeypress(move_right, "Right")
# wn.onkeypress(fire_bullet, "space")

# # Main game loop
# while True:
#     wn.update()

#     # Move the aliens down
#     for alien in aliens:
#         alien.sety(alien.ycor() - 2)

#         # Check if the alien is at the bottom
#         if alien.ycor() < -290:
#             alien.goto(random.randint(-290, 290), random.randint(100, 250))

#         # Check for collision with the bullet
#         if is_collision(bullet, alien):
#             bullet.hideturtle()
#             bullet.goto(0, -240)
#             bullet_state = "ready"
#             alien.goto(random.randint(-290, 290), random.randint(100, 250))

#     # Move the bullet
#     if bullet_state == "fire":
#         bullet.sety(bullet.ycor() + 20)

#     # Check if bullet has gone off the screen
#     if bullet.ycor() > 300:
#         bullet.hideturtle()
#         bullet_state = "ready"

# wn.mainloop()


# import turtle
# import random
# window = turtle.Screen()
# window.title('robot')
# window.bgcolor('black')
# window.setup(width=800, height=1000)

# Mainchara=turtle.Turtle()
# window.addshape(r'/Users/mac/Desktop/final-report/mainchara.gif')
# Mainchara.shape(r'/Users/mac/Desktop/final-report/mainchara.gif')
# Mainchara.goto(-0,-300)


# Laser=turtle.Turtle()
# window.addshape(r'/Users/mac/Desktop/final-report/laser  .gif')
# Laser.shape(r'/Users/mac/Desktop/final-report/laser  .gif')
# Laser.goto(-0,-210)
# Laser.hideturtle()
# Laser_state='ready'


# Aliens = []
# for _ in range(5):
#     Alien=turtle.Turtle()
#     window.addshape(r'/Users/mac/Desktop/final-report/e1 .gif')
#     Alien.shape(r'/Users/mac/Desktop/final-report/e1 .gif')
#     Alien.goto(random.randint(-290, 290), random.randint(100, 250))
#     Aliens.append(Alien)

# def trai():
#     x = Mainchara.xcor()
#     x -= 20
#     if x < -280:
#         x = -280
#     Mainchara.setx(x)

# def phai():
#     x = Mainchara.xcor()
#     x += 20
#     if x < 280:
#         x = 280
#     Mainchara.setx(x)

# def fire_bullet():
#     if  Laser_state == "ready":
#         Laser_state = "fire"
#         Laser.goto(Mainchara.xcor(), Mainchara.ycor() + 20)
#         Laser.showturtle()
#     return Laser

# window.listen()
# window.onkeypress(trai,'A')
# window.onkeypress(phai,'D')
# window.onkeypress(fire_bullet,'space')







# window.mainloop()







import turtle
import random

# Set up the window
window = turtle.Screen()
window.title('Robot Space Shooter')
window.bgcolor('black')
window.setup(width=800, height=1000)

# Scoreboard setup
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.scoreboard = turtle.Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 400)
        self.update_score()

    def update_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increment_score(self):
        self.score += 10
        self.update_score()

# Main character setup
class MainCharacter:
    def __init__(self):
        self.character = turtle.Turtle()
        window.addshape(r'/Users/mac/Desktop/final-report/mainchara.gif')
        self.character.shape(r'/Users/mac/Desktop/final-report/mainchara.gif')
        self.character.penup()
        self.character.goto(0, -400)

    def move_left(self):
        x = self.character.xcor()
        x -= 20
        if x < -380:
            x = -380
        self.character.setx(x)

    def move_right(self):
        x = self.character.xcor()
        x += 20
        if x > 380:
            x = 380
        self.character.setx(x)

# Laser setup
class Laser:
    def __init__(self):
        self.laser = turtle.Turtle()
        window.addshape(r'/Users/mac/Desktop/final-report/laser  .gif')
        self.laser.shape(r'/Users/mac/Desktop/final-report/laser  .gif')
        self.laser.penup()
        self.laser.hideturtle()
        self.state = 'ready'

    def fire(self, x, y):
        if self.state == "ready":
            self.state = "fire"
            self.laser.goto(x, y + 20)
            self.laser.showturtle()

    def move(self):
        if self.state == "fire":
            y = self.laser.ycor()
            self.laser.sety(y + 20)
            if y > 500:
                self.laser.hideturtle()
                self.state = "ready"

# Alien setup
class Alien:
    def __init__(self):
        self.alien = turtle.Turtle()
        window.addshape(r'/Users/mac/Desktop/final-report/e1 .gif')
        self.alien.shape(r'/Users/mac/Desktop/final-report/e1 .gif')
        self.alien.penup()
        self.reset_position()

    def reset_position(self):
        self.alien.goto(random.randint(-290, 290), random.randint(100, 400))

    def move(self):
        y = self.alien.ycor()
        y -= 2
        self.alien.sety(y)
        if y < -500:
            self.reset_position()

# Main game loop
def main():
    scoreboard = Scoreboard()
    main_character = MainCharacter()
    laser = Laser()
    aliens = [Alien() for _ in range(5)]

    # Key bindings
    window.listen()
    window.onkeypress(main_character.move_left, 'a')
    window.onkeypress(main_character.move_right, 'd')

    def fire_bullet():
        laser.fire(main_character.character.xcor(), main_character.character.ycor())

    window.onkeypress(fire_bullet, 'space')

    # Game loop
    while True:
        window.update()
        laser.move()  # Move the laser
        for alien in aliens:
            alien.move()  # Move the aliens

            # Check for collisions
            if laser.laser.distance(alien.alien) < 20 and laser.state == "fire":
                alien.reset_position()  # Respawn alien
                laser.laser.hideturtle()  # Hide laser
                laser.state = "ready"  # Reset laser state
                scoreboard.increment_score()  # Update score

window.mainloop()  # Keep the window open

