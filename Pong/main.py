import turtle
#import time
import random
#import tkinter as tk

FONT = ("Courier", 24, "normal")

def draw_screen(choice):
    s = turtle.getscreen()
    s.title("Pong")
    s.bgcolor(choice)
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

def draw_paddle():
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

def draw_button():
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

def move_ball(s, b, l, r, score, b1):
    b.dx = 8
    b.dy = 8
    def update_ball():
        b.setx(b.xcor() + b.dx)
        b.sety(b.ycor() + b.dy)
        #if b.ycor() > 290:
        #    b.sety(290)
        #    b.dy *= -1
        #if b.ycor() < -290:
        #    b.sety(-290)
        #    b.dy *= -1
        if abs(b.ycor()) > 290:
            b.dy *= -1
        if b.xcor() < -340 and l.ycor() - 50 < b.ycor() < l.ycor() + 50:
            b.setx(-340)
            b.dx *= -1
        if b.xcor() > 340 and r.ycor() - 50 < b.ycor() < r.ycor() + 50:
            b.setx(340)
            b.dx *= -1
        if b.xcor() > 390:
            reset_ball(b)
            update_score(score, "left", s, b, l, r, b1)
        if b.xcor() < -390:
            reset_ball(b)
            update_score(score, "right", s, b, l, r, b1)
        s.ontimer(update_ball, 20)
    update_ball()

def listen_paddle(s, l, r):
    s.onkey(lambda: l.sety(l.ycor()+50), "w")
    s.onkey(lambda: l.sety(l.ycor()-50), "s")
    s.onkey(lambda: r.sety(r.ycor()+50), "Up")
    s.onkey(lambda: r.sety(r.ycor()-50), "Down")
    s.listen()
    def update_paddle():
        if l.ycor() > 250:
            l.sety(l.ycor()-50)
        if l.ycor() < -250:
            l.sety(l.ycor()+50) 
        if r.ycor() > 250:
            r.sety(r.ycor()-50)
        if r.ycor() < -250:
            r.sety(r.ycor()+50)
        s.ontimer(update_paddle, 20)
    update_paddle()

def reset_ball(b):
    b.goto(0, 0)
    b.dx *= 1

def restart(s, l, r, b1, b, score):
    score.clear()
    score.goto(0, 320)
    score.write("Player Left: 0  Player Right: 0", align="center", font=FONT)
    update_score.left = 0
    update_score.right = 0
    move_ball(s, b, l, r, score, b1)

def game_over(score, player, s, b, l, r, b1):
    b.dx, b.dy = 0, 0
    score.clear()
    score.goto(0, 50)
    score.write(f"{player} player wins! 'R' to restart.", align="center", font=FONT)
    s.onkey(lambda: restart(s, l, r, b1, b, score), "r")
    s.mainloop()
   
def update_score(score, player, s, b, l, r, b1):
    score.clear()
    if player == "left":
        update_score.left += 1
    elif player == "right":
        update_score.right += 1
    score.write(f"Player Left: {update_score.left} Player Right: {update_score.right}", align="center", font=FONT)
    if update_score.left == 3 or update_score.right == 3:
        game_over(score, player, s, b, l, r, b1)

def initialize(choice):
    update_score.left = 0
    update_score.right = 0
    s = draw_screen(choice)
    draw_border()
    b = draw_ball()
    score = draw_score()
    l, r = draw_paddle()
    b1 = draw_button()
    b1.onclick(lambda x, y: start(s, l, r, b1, b, score))
    s.mainloop()

def start(s, l, r, b1, b, score):
    b1.clear()
    b1.hideturtle()
    listen_paddle(s, l, r)
    move_ball(s, b, l, r, score, b1)
    s.mainloop()

def main():
    colors = ["red", "blue", "green", "purple", "orange", "black"]
    #print(colors)
    #choice = int(input("Choose a color (0-5): "))
    #while choice < 0 or choice > 5:
    #    choice = int(input("Invalid choice. Choose a color (0-5): "))
    #choice = colors[choice]
    #initialize(choice)
    choice = random.choice(colors)
    initialize(choice)

    #todo: Pause, Game over, Quit game, Neural Network, Color Customisation

if __name__ == "__main__":
    main()
