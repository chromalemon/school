import turtle
#import time
#import random
#import tkinter as tk

FONT = ("Courier", 24, "normal")

def start(s, b, l, r, score, b1, paused):
    def toggle_pause():
        nonlocal paused
        paused = not paused
        b1.clear()
        if paused:
            b1.write("START", align="center", font=FONT)
            move_ball(s, b, l, r, score, paused)
            move_paddle(s, l, r, paused)
        else:
            b1.write("PAUSE", align="center", font=FONT)
            move_ball(s, b, l, r, score, paused)
            move_paddle(s, l, r, paused)
    b1.onclick(lambda x, y: toggle_pause())
    s.mainloop()

def draw_screen():
    s = turtle.getscreen()
    s.title("Pong")
    s.bgcolor("black")
    return s

def draw_border():
    b = turtle.Turtle()
    b.speed(0)
    b.color("white")
    b.pensize(3)
    b.penup()
    b.goto(-400, 300)
    b.pendown()
    for _ in range(2):
        b.forward(800)
        b.right(90)
        b.forward(600)
        b.right(90)
    b.hideturtle()

def draw_ball():
    b = turtle.Turtle()
    b.color("white")
    b.shape("square")
    b.penup()
    return b

def draw_paddles():
    l = turtle.Turtle()
    l.color("white")
    l.shape("square")
    l.shapesize(stretch_wid=5, stretch_len=1)
    l.penup()
    l.goto(-350, 0)
    l.speed(0)
    r = turtle.Turtle()
    r.color("white")
    r.shape("square")
    r.shapesize(stretch_wid=5, stretch_len=1)
    r.penup()
    r.goto(350, 0)
    r.speed(0)
    return l, r

def draw_score():
    score = turtle.Turtle()
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0, 320)
    score.write("Player Left: 0  Player Right: 0", align="center", font=FONT)
    return score

def draw_button(s, b, l, r, score):
    b1 = turtle.Turtle()
    b1.fillcolor("")
    b1.shape("square")
    b1.pencolor("white")
    b1.pensize(2)
    b1.penup()
    b1.goto(0,420)
    b1.shapesize(stretch_wid=5, stretch_len=10)
    b1.write("START", align="center", font=FONT)
    return b1

def move_ball(s, b, l, r, score, paused):
    b.dx = 8
    b.dy = 8
    def update_ball(paused):
        if not paused:
            b.setx(b.xcor() + b.dx)
            b.sety(b.ycor() + b.dy)
            if b.ycor() > 290:
                b.sety(290)
                b.dy *= -1
            if b.ycor() < -290:
                b.sety(-290)
                b.dy *= -1
            if b.xcor() < -340 and l.ycor() - 50 < b.ycor() < l.ycor() + 50:
                b.setx(-340)
                b.dx *= -1
            if b.xcor() > 340 and r.ycor() - 50 < b.ycor() < r.ycor() + 50:
                b.setx(340)
                b.dx *= -1
            if b.xcor() > 390:
                reset_ball(b)
                update_score(score, "left")
            if b.xcor() < -390:
                reset_ball(b)
                update_score(score, "right")
            s.ontimer(update_ball(paused), 20)
    update_ball(paused)

def move_paddle(s, l, r, paused):
    s.onkey(lambda: l.sety(l.ycor()+50), "w")
    s.onkey(lambda: l.sety(l.ycor()-50), "s")
    s.onkey(lambda: r.sety(r.ycor()+50), "Up")
    s.onkey(lambda: r.sety(r.ycor()-50), "Down")
    s.listen()
    def update_paddle(paused):
        if not paused:
            if l.ycor() > 250:
                l.sety(l.ycor()-50)
            if l.ycor() < -250:
                l.sety(l.ycor()+50) 
            if r.ycor() > 250:
                r.sety(r.ycor()-50)
            if r.ycor() < -250:
                r.sety(r.ycor()+50)
            s.ontimer(update_paddle(paused), 20)
    update_paddle(paused)  

def reset_ball(b):
    b.goto(0, 0)
    b.dx *= -1

def update_score(score, player):
    score.clear()
    if player == "left":
        update_score.left += 1
    elif player == "right":
        update_score.right += 1
    score.write(f"Player Left: {update_score.left} Player Right: {update_score.right}", align="center", font=FONT)

def initialize():
    paused = True
    s = draw_screen()
    draw_border()
    b = draw_ball()
    l, r = draw_paddles()
    score = draw_score()
    b1 = draw_button(s, b, l, r, score)
    start(s, b, l, r, score, b1, paused)

def main():
    initialize()
    #todo: Pause, Game over, Quit game, Neural Network, Color Customisation

if __name__ == "__main__":
    main()
