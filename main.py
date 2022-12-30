from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

right_paddle=Paddle((370,0))
left_paddle=Paddle((-380,0))

#Ball
ball=Ball()

#Score
score=Score()
#Keyboard controls

screen.listen()
screen.onkey(right_paddle.up,'Up')
screen.onkey(right_paddle.down,'Down')

screen.onkey(left_paddle.up,'w')
screen.onkey(left_paddle.down,'s')

is_game_on=True

while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    #Detect collosion
    if ball.ycor()>279 or ball.ycor()<-279:
        ball.bounce_y()

    #Collosion with the paddels
    if ball.distance(right_paddle)<60 and ball.xcor()>340:
        ball.bounce_x()
    elif  ball.distance(left_paddle)<50 and ball.xcor()<-350:
        ball.bounce_x()

    #right paddle misses
    if ball.xcor()>390:
        ball.reset_position()
        score.l_point()

    #left paddle misses
    if ball.xcor()<-390:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
