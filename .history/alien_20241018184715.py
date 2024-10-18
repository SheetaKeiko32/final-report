# # # import turtle
# # # import random

# # # # Setup the screen
# # # wn = turtle.Screen()
# # # wn.title("Alien Drop")
# # # wn.bgcolor("black")
# # # wn.setup(width=600, height=600)

# # # # Player
# # # player = turtle.Turtle()
# # # player.speed(0)
# # # player.shape("square")
# # # player.color("green")
# # # player.penup()
# # # player.goto(0, -250)
# # # player.shapesize(stretch_wid=1, stretch_len=3)

# # # # Bullet
# # # bullet = turtle.Turtle()
# # # bullet.speed(0)
# # # bullet.shape("triangle")
# # # bullet.color("red")
# # # bullet.penup()
# # # bullet.hideturtle()
# # # bullet.goto(0, -240)
# # # bullet.setheading(90)
# # # bullet_state = "ready"

# # # # Aliens
# # # aliens = []
# # # for _ in range(5):
# # #     alien = turtle.Turtle()
# # #     alien.speed(0)
# # #     alien.shape("circle")
# # #     alien.color("orange")
# # #     alien.penup()
# # #     alien.goto(random.randint(-290, 290), random.randint(100, 250))
# # #     aliens.append(alien)

# # # # Functions
# # # def move_left():
# # #     x = player.xcor()
# # #     x -= 20
# # #     if x < -280:
# # #         x = -280
# # #     player.setx(x)

# # # def move_right():
# # #     x = player.xcor()
# # #     x += 20
# # #     if x > 280:
# # #         x = 280
# # #     player.setx(x)

# # # def fire_bullet():
# # #     global bullet_state
# # #     if bullet_state == "ready":
# # #         bullet_state = "fire"
# # #         bullet.goto(player.xcor(), player.ycor() + 10)
# # #         bullet.showturtle()

# # # def is_collision(t1, t2):
# # #     return t1.distance(t2) < 20

# # # # Keyboard bindings
# # # wn.listen()
# # # wn.onkeypress(move_left, "Left")
# # # wn.onkeypress(move_right, "Right")
# # # wn.onkeypress(fire_bullet, "space")

# # # # Main game loop
# # # while True:
# # #     wn.update()

# # #     # Move the aliens down
# # #     for alien in aliens:
# # #         alien.sety(alien.ycor() - 2)

# # #         # Check if the alien is at the bottom
# # #         if alien.ycor() < -290:
# # #             alien.goto(random.randint(-290, 290), random.randint(100, 250))

# # #         # Check for collision with the bullet
# # #         if is_collision(bullet, alien):
# # #             bullet.hideturtle()
# # #             bullet.goto(0, -240)
# # #             bullet_state = "ready"
# # #             alien.goto(random.randint(-290, 290), random.randint(100, 250))

# # #     # Move the bullet
# # #     if bullet_state == "fire":
# # #         bullet.sety(bullet.ycor() + 20)

# # #     # Check if bullet has gone off the screen
# # #     if bullet.ycor() > 300:
# # #         bullet.hideturtle()
# # #         bullet_state = "ready"

# # # wn.mainloop()


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

# Alien1=turtle.Turtle()
# Alien = []
# for _ in range(5):
#     window.addshape(r'/Users/mac/Desktop/final-report/e1 .gif')
#     Alien1.shape(r'/Users/mac/Desktop/final-report/e1 .gif')
#     Alien.goto(random.randint(-290, 290), random.randint(100, 250))
#     Alien1.append(Alien1)

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

# def fire_bullet(Laser):
#     if  Laser == "ready":
#         Laser = "fire"
#         Laser.goto(Mainchara.xcor(), Mainchara.ycor() + 10)
#         Laser.showturtle()
#     return Laser


# window.listen()
# window.onkey()

# window.mainloop()
import turtle
import random

# Set up the window
window = turtle.Screen()
window.title('Robot')
window.bgcolor('black')
window.setup(width=800, height=1000)

# Main character setup
Mainchara = turtle.Turtle()
window.addshape('/Users/mac/Desktop/final-report/mainchara.gif')
Mainchara.shape('/Users/mac/Desktop/final-report/mainchara.gif')
Mainchara.goto(0, -300)  # Use 0 instead of -0 for clarity

# Laser setup
Laser = turtle.Turtle()
window.addshape('/Users/mac/Desktop/final-report/laser.gif')  # Remove extra spaces in filename
Laser.shape('/Users/mac/Desktop/final-report/laser.gif')
Laser.goto(0, -210)
Laser.hideturtle()
Laser_state = 'ready'

# Alien setup
Aliens = []  # Changed to a list for storing multiple aliens
for _ in range(5):
    Alien = turtle.Turtle()
    window.addshape('/Users/mac/Desktop/final-report/e1.gif')  # Remove extra spaces in filename
    Alien.shape('/Users/mac/Desktop/final-report/e1.gif')
    Alien.goto(random.randint(-290, 290), random.randint(100, 250))
    Aliens.append(Alien)  # Append the new alien to the list

# Movement functions
def trai():
    x = Mainchara.xcor()
    x -= 20
    if x < -280:
        x = -280
    Mainchara.setx(x)

def phai():
    x = Mainchara.xcor()
    x += 20
    if x > 280:  # Changed < to > for the right boundary
        x = 280
    Mainchara.setx(x)

def fire_bullet():
    global Laser_state  # Declare Laser_state as global
    if Laser_state == "ready":
        Laser_state = "fire"
        Laser.goto(Mainchara.xcor(), Mainchara.ycor() + 10)
        Laser.showturtle()

# Key bindings
window.listen()
window.onkey(trai, "Left")  # Bind left arrow key to trai function
window.onkey(phai, "Right")  # Bind right arrow key to phai function
window.onkey(fire_bullet, "space")  # Bind space bar to fire_bullet function

# Main loop
window.mainloop()
