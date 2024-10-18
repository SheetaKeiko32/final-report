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

# # def fire_bullet():
# #     if  Laser_state == "ready":
# #         Laser_state = "fire"
# #         Laser.goto(Mainchara.xcor(), Mainchara.ycor() + 10)
# #         Laser.showturtle()
# #     return Laser

# window.listen()
# window.onkeypress(trai,'A')
# window.onkeypress(phai,'D')
# # window.onkeypress(fire_bullet,'space')


# window.mainloop()
import turtle
import random
import time

# Set up the window
window = turtle.Screen()
window.title('Robot Space Shooter')
window.bgcolor('black')
window.setup(width=800, height=1000)

# Scoreboard setup
score = 0
scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 400)
scoreboard.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Main character setup
Mainchara = turtle.Turtle()
window.addshape(r'/Users/mac/Desktop/final-report/mainchara.gif')
Mainchara.shape(r'/Users/mac/Desktop/final-report/mainchara.gif')
Mainchara.penup()
Mainchara.goto(0, -400)

# Laser setup
Laser = turtle.Turtle()
window.addshape(r'/Users/mac/Desktop/final-report/laser  .gif')
Laser.shape(r'/Users/mac/Desktop/final-report/laser  .gif')
Laser.penup()
Laser.hideturtle()
laser_state = 'ready'

# Alien setup
Aliens = []
for _ in range(5):
    Alien = turtle.Turtle()
    window.addshape(r'/Users/mac/Desktop/final-report/e1 .gif')
    Alien.shape(r'/Users/mac/Desktop/final-report/e1 .gif')
    Alien.penup()
    Alien.goto(random.randint(-290, 290), random.randint(100, 400))
    Aliens.append(Alien)

# Movement functions
def trai():
    x = Mainchara.xcor()
    x -= 20
    if x < -380:
        x = -380
    Mainchara.setx(x)

def phai():
    x = Mainchara.xcor()
    x += 20
    if x > 380:
        x = 380
    Mainchara.setx(x)

def fire_bullet(laser_state, last_shot_time):
    current_time = time.time()
    if laser_state == "ready" and (current_time - last_shot_time >= 1.5):
        laser_state = "fire"
        Laser.goto(Mainchara.xcor(), Mainchara.ycor() + 20)
        Laser.showturtle()
        last_shot_time = current_time
    return laser_state, last_shot_time

def move_bullet(laser_state):
    if laser_state == "fire":
        y = Laser.ycor()
        Laser.sety(y + 20)
        if y > 500:  # Hide the laser if it goes off the screen
            Laser.hideturtle()
            laser_state = "ready"
    return laser_state

def move_aliens():
    for alien in Aliens:
        y = alien.ycor()
        y -= 2  # Move the alien downward
        alien.sety(y)

        # Reset alien if it goes off the screen
        if y < -500:
            alien.goto(random.randint(-290, 290), random.randint(100, 400))

def check_collision(laser_state):
    global score
    for alien in Aliens:
        if Laser.distance(alien) < 20:  # Collision detection
            # Reset the alien's position and update the score
            alien.goto(random.randint(-290, 290), 400)  # Respawn at the top
            Laser.hideturtle()
            laser_state = "ready"
            score += 10
            scoreboard.clear()
            scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    return laser_state

# Key bindings
window.listen()
window.onkeypress(trai, 'a')
window.onkeypress(phai, 'd')
window.onkeypress(lambda: fire_bullet(laser_state, last_shot_time), 'space')  # Fire on space

# Main loop
last_shot_time = 0  # To track the last shot time
while True:
    window.update()
    laser_state = move_bullet(laser_state)  # Update laser state
    laser_state, last_shot_time = fire_bullet(laser_state, last_shot_time)  # Handle bullet firing
    move_aliens()  # Update alien positions
    laser_state = check_collision(laser_state)  # Check for collisions

window.mainloop()  # Keep the window open


