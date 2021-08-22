# Simple Pong game in Python 3 for Beginners
# Part 1 : Getting started

import turtle
import winsound
import textwrap

wn = turtle.Screen()  # create a screen for the game.
wn.title("Pong by @john.yshiro")  # title for the game.
wn.bgcolor("Black")  # change the title color.
wn.setup(width=800, height=600)  # Setup the width and height.
wn.tracer(0)  # Stop the window from updating and that increase the game speed.

# Score
score_a = 0
score_b = 0

# Paddle 1
paddle_a = turtle.Turtle()
paddle_a.shape("square")  # The shape can be square, circle and triangle
paddle_a.speed(0)  # The speed of the animation, we need for the turtle module
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # This will let the program to draw automatically
paddle_a.goto(-350, 0)  # The paddle a start from x=-350 and y=0


# Paddle 2
paddle_b = turtle.Turtle()
paddle_b.shape("square")  # The shape can be square, circle and triangle
paddle_b.speed(0)  # The speed of the animation, we need for the turtle module
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # This will let the program to draw automatically
paddle_b.goto(350, 0)  # The paddle a start from x=350 and y=0

# Ball
ball = turtle.Turtle()
ball.shape("square")  # The shape can be square, circle and triangle
ball.speed(0)  # The speed of the animation, we need for the turtle module
ball.color("white")
ball.penup()  # This will let the program to draw automatically
ball.goto(0, 0)  # The paddle a start from x=-350 and y=0
ball.dx = 0.5
ball.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# Pen Result
penResult = turtle.Turtle()
penResult.speed(0)
penResult.color("white")
penResult.penup()
penResult.hideturtle()
penResult.goto(0, 0)


# Function


def paddle_a_up():
    y = paddle_a.ycor()  # Turtle module return the y coordinate of paddle a
    y += 20
    # Set the value of new y to paddle a to change the position
    paddle_a.sety(y)
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
        paddle_a.dy *= -1


def paddle_a_down():
    y = paddle_a.ycor()  # Turtle module return the y coordinate of paddle a
    y -= 20
    # Set the value of new y to paddle a to change the position
    paddle_a.sety(y)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
        paddle_a.dy *= -1


def paddle_b_up():
    y = paddle_b.ycor()  # Turtle module return the y coordinate of paddle a
    y += 20
    # Set the value of new y to paddle a to change the position
    paddle_b.sety(y)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
        paddle_b.dy *= -1


def paddle_b_down():
    y = paddle_b.ycor()  # Turtle module return the y coordinate of paddle a
    y -= 20
    # Set the value of new y to paddle a to change the position
    paddle_b.sety(y)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
        paddle_b.dy *= -1


# Keyboard binding
wn.listen()

# Press on keyboard letter w to move the paddle a up
wn.onkeypress(paddle_a_up, "w")
# Press on keyboard letter s to move the paddle a down
wn.onkeypress(paddle_a_down, "s")
# Press on arrow Up to move the paddle b up
wn.onkeypress(paddle_b_up, "Up")
# Press on arrow Down to move the paddle b down
wn.onkeypress(paddle_b_down, "Down")

# Main game loop (every game has this loop)
while True:
    wn.update()  # every time the loop start it will update the screen.

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # End the game
    if score_a == 10:
        pen.clear()
        penResult.write("Player A: {}  Player B: {}, \nPlayer A Won!".format(score_a, score_b), align="center",
                        font=("Courier", 24, "normal"))

    if score_b == 10:
        pen.clear()
        penResult.write("Player A: {}  Player B: {}, \nPlayer B Won!".format(score_a, score_b), align="center",
                        font=("Courier", 24, "normal"))

    # Paddle and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
