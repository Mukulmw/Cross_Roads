import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            newcar = Turtle()
            newcar.shape("square")
            newcar.penup()
            newcar.color(random.choice(COLORS))
            newcar.shapesize(stretch_wid=1, stretch_len=2)
            newcar.teleport(x=280, y=random.randint(a =-250, b =250))
            newcar.setheading(180)
            self.cars.append(newcar)

    def increase_speed(self):

        self.speed += MOVE_INCREMENT
    def move_cars(self):
        global speed
        for car in self.cars:
            car.forward(self.speed)

            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)







