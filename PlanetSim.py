import turtle
import math
import time

class Planet:
    def __init__(self, name, size, color, distance, speed):
        self.name = name
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.shape("circle")
        self.turtle.shapesize(size, size, 0)
        self.turtle.color(color)
        self.distance = distance
        self.speed = speed

    def orbit_around_sun(self):
        angle = self.turtle.heading()
        angle += self.speed
        x = self.distance * math.cos(math.radians(angle))
        y = self.distance * math.sin(math.radians(angle))
        self.turtle.goto(x, y)
        self.turtle.setheading(angle)

# Screen
win = turtle.Screen()
win.title("Planet Sim")
win.bgcolor("black")
win.setup(height=800, width=800)
win.tracer(2)


frame_rate = 240
frame_delay = 1 / frame_rate

# Create Planets
sun = Planet("Sun", 2, "#fdb813", 0, 0)
mercury = Planet("Mercury", 0.2, "dark gray", 68, 1.70505)
venus = Planet("Venus", 0.5, "#ffde38", 107, 1.26077)
earth = Planet("Earth", 0.52, "blue", 148, 1.07000)
mars = Planet("Mars", 0.3, "#bd6d53", 234, 0.86871)

# Main Loop
while True:
    for planet in [mercury, venus, earth, mars]:
        planet.orbit_around_sun()
    win.update()

    time.sleep(frame_delay)
