import turtle
import random

wn = turtle.Screen()
wn.title('The Breakout Game')
wn.screensize(600, 600)

class Breaks(turtle.Turtle):

    def __init__(self, num):
        x_positions = [x for x in range(-300, 301, 120)]
        y_positions = [y for y in range(100, 301, 50)]
        positions = []
        for x in x_positions:
            for y in y_positions:
                positions.append((x, y))

        super().__init__()
        colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown']
        self.shape('square')
        self.color(random.choice(colors))
        self.shapesize(2, 5, 2)
        self.penup()
        self.setpos(positions[num])


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('black')
        self.shapesize(1,1,5)
        self.penup()
        self.goto(random.choice([-250]),-290)
        self.speed(1.5)
        #self.setheading(90)

    def move(self):
       self.forward(20)

    def hit_wall(self, x, y):
        self.setx(-1* self.xcor())

    def bounce(self):
        self.sety(-1 * self.ycor() + 10)


    def collision(self):
        for prick in pricks:
            if ball.ycor() > 150:
                if ball.xcor() >= prick.xcor() - 20:
                    if ball.xcor() >= prick.xcor() + 20:
                        if ball.ycor() >= prick.ycor() + 20:
                            prick.hideturtle()
                            ball.bounce()
                            return True


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.shapesize(1,7)
        self.penup()
        self.setpos(0,-300)

    def go_right(self):
        if self.xcor() < 280:
            return self.setx(self.xcor() + 20)
        else:
            pass

    def go_left(self):
        if self.xcor() > -280:
            return self.setx(self.xcor() -20)
        else:
            pass

player = Player()

wn.onkey(player.go_right,'Right')
wn.onkey(player.go_left, 'Left')
wn.listen()



pricks = []
for i in range(10):
    pricks.append(Breaks(i))

ball = Ball()


while True:
    tx, ty = -250, 300
    dy = 1
    dx = random.choice([-.5, .5])
    targets = []

    def __init__(self):
        wn.tracer(0)
        self.pl = Player()
        self.ball = Ball()
        wn.tracer(1)


    if ball.ycor() < -300:
        exit()
    if ball.ycor() > 300:
        dy *= -1

    if ball.ycor() >= 175:
        for prick in pricks:
            if not prick.white:
                if ball.ycor() >= prick.ycor() - 25:
                    if ball.xcor() >= prick.xcor() - 25:
                        if ball.xcor() <= prick.xcor() + 25:
                            dy *= -1
                            prick.color('white')
                            prick.white = True
                            break

    if ball.xcor() <= -270 or ball.xcor() >= 260:
        dx *= -1
    if ball.ycor() <= player.ycor() + 25:
        if ball.xcor() >= player.xcor() - 50:
            if ball.xcor() <= player.xcor() + 50:
                dy *= -1
    ball.setpos(ball.xcor() + dx * 3, ball.ycor() - dy * 3)


# wn.mainloop()
#wn.exitonclick()
