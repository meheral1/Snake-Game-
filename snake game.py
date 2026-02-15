import turtle
import time
import random

delay = 0.11
score = 0

# High Score load karna
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 0

# Game screen setup
screen = turtle.Screen()
screen.title("Snake Game - No Borders Edition")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
s_head = turtle.Turtle()
s_head.speed(0)
s_head.color("white")
s_head.shape("square")
s_head.penup()
s_head.goto(0, 0)
s_head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

body = []

# Scoring setup
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-280, 260)
# Shuru mein hi high score dikhana zaroori hai
pen.write(f"Score: {score}  High Score: {high_score}", align="left", font=("Arial", 14, "bold"))

# Directions with 180-degree turn protection
def go_up():
    if s_head.direction != "down":
        s_head.direction = "up"
def go_down():
    if s_head.direction != "up":
        s_head.direction = "down"
def go_left():
    if s_head.direction != "right":
        s_head.direction = "left"
def go_right():
    if s_head.direction != "left":
        s_head.direction = "right"

# Movement logic
def move():
    if s_head.direction == "up":
        s_head.sety(s_head.ycor() + 20)
    if s_head.direction == "down":
        s_head.sety(s_head.ycor() - 20)
    if s_head.direction == "left":
        s_head.setx(s_head.xcor() - 20)
    if s_head.direction == "right":
        s_head.setx(s_head.xcor() + 20)

# Key bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main Loop
while True:
    screen.update()

    # Border Teleportation
    if s_head.xcor() > 290: s_head.setx(-290)
    elif s_head.xcor() < -290: s_head.setx(290)
    if s_head.ycor() > 290: s_head.sety(-290)
    elif s_head.ycor() < -290: s_head.sety(290)

    # Food Collision
    if s_head.distance(food) < 20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
        
        # New body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        body.append(new_segment)

        # Update Score
        score += 1
        if score > high_score:
            high_score = score
            with open("highscore.txt", "w") as f:
                f.write(str(high_score))
        
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="left", font=("Arial", 14, "bold"))

    # Move body segments in reverse order
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

    # Move segment 0 to head
    if len(body) > 0:
        body[0].goto(s_head.xcor(), s_head.ycor())

    move()

    # Body Collision
    for segment in body[1:]: # Pehle segment ko ignore maaro
        if segment.distance(s_head) < 20:
            time.sleep(1)
            s_head.goto(0, 0)
            s_head.direction = "stop"
            
            # Cleanup segments
            for seg in body:
                seg.goto(1000, 1000)
                seg.hideturtle()
            body.clear()
            
            # Reset score
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="left", font=("Arial", 14, "bold"))

    time.sleep(delay)

screen.mainloop()