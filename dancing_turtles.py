import turtle
import math
import time

screen = turtle.Screen()
screen.title("Dancing Turtles")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

COLORS = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta"]
NUM_TURTLES = 8
turtles = []

for i in range(NUM_TURTLES):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(COLORS[i % len(COLORS)])
    t.penup()
    t.speed(0)
    turtles.append(t)

angle_step = 2 * math.pi / NUM_TURTLES
frame = 0

def dance():
    global frame
    t_val = frame * 0.05

    for i, t in enumerate(turtles):
        base_angle = angle_step * i + t_val
        radius = 150 + 60 * math.sin(t_val * 2 + i)

        x = radius * math.cos(base_angle)
        y = radius * math.sin(base_angle)

        t.goto(x, y)
        t.setheading((base_angle * 180 / math.pi + 90) % 360)

        # Bob up and down
        bob = 20 * math.sin(t_val * 3 + i * 0.8)
        t.goto(x, y + bob)

        # Size pulse using turtlesize
        scale = 1.5 + 0.5 * math.sin(t_val * 2 + i)
        t.turtlesize(scale)

    screen.update()
    frame += 1
    screen.ontimer(dance, 16)

dance()
turtle.done()
