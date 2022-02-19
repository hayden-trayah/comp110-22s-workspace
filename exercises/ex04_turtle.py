"""Turtle drawing of a city skyline during a crisp Febuary dusk. Skyscraper function incorporates simpler component procedure (part 7) - lines 9-18. Moon utilizes a turtle function not covered in tutorial (part 8) - line 111."""

from turtle import Turtle, colormode, done
__author__ = "730325581"

colormode(255)


def skyscraper_builder(leo: Turtle, width: float, height: float) -> None:
    """Component procedure used to simplify skyscraper function."""
    i: int = 1
    while i < 3:
        leo.forward(width)
        leo.left(90)
        leo.forward(height)
        leo.left(90)
        i = i + 1
    leo.end_fill()


def skyscraper(leo: Turtle, x: float, y: float, width: float, height: float, r: float, g: float, b: float) -> None:
    """Builds a monumental and intimidating skyscraper."""
    leo.color(r, g, b)
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.speed(200)
    leo.begin_fill()
    skyscraper_builder(leo, width, height)
    leo.end_fill()


def background(leo: Turtle, x: float, y: float, width: float, height: float, r: float, g: float, b: float) -> None:
    """Builds a dark, mystic, and crisp night sky."""
    leo.color(r, g, b)
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.speed(200)
    i: int = 1
    leo.begin_fill()
    while i < 3:
        leo.forward(width)
        leo.left(90)
        leo.forward(height)
        leo.left(90)
        i = i + 1
    leo.end_fill()


def create_star(leo: Turtle, x: float, y: float, r: float, g: float, b: float) -> None:
    """Draws a beautiful five-pointed star."""
    # create_star(leo, -100, 100, 255, 251, 176)
    leo.color(r, g, b)
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.speed(200)
    i: int = 6
    leo.begin_fill()
    while i > 0:
        leo.forward(25)
        leo.left(145)
        i -= 1
    leo.end_fill()
    # leo.penup()


def rectangle(leo: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Builds a beatiful slim rectangle used as antennas and windows."""
    leo.color(211, 211, 211)
    leo.pencolor("black")
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.speed(200)
    i: int = 1
    leo.begin_fill()
    while i < 3:
        leo.forward(width)
        leo.left(90)
        leo.forward(height)
        leo.left(90)
        i = i + 1
    leo.end_fill()


def window(leo: Turtle, x: float, y: float, width: float) -> None:
    """Draws an eloquent square window."""
    leo.color(255, 255, 255)
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.speed(200)
    leo.begin_fill()
    i: int = 0
    while i < 3:
        leo.forward(width)
        leo.left(90)
        i = i + 1
    leo.end_fill()


def moon(leo: Turtle, x: float, y: float, size: float, r: float, g: float, b: float) -> None:
    """Draws an aboslutely gnarly moon to light up the night sky - This is me using a function that was not described in the tutorial."""
    leo.color(r, g, b)
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.begin_fill()
    leo.circle(size)
    leo.end_fill()


def main() -> None:
    """The entrypoint of my epic skyscraper scene."""
    leo: Turtle = Turtle()
    background(leo, -500, -300, 1000, 1000, 21, 34, 56)
    skyscraper(leo, -300, -300, 180, 420, 0, 0, 0)
    skyscraper(leo, -100, -300, 180, 350, 165, 165, 165)
    skyscraper(leo, 100, -300, 180, 375, 128, 128, 128)
    rectangle(leo, 150, 75, 5, 100)
    rectangle(leo, 175, 75, 5, 75)
    rectangle(leo, 200, 75, 5, 125)
    window(leo, 15, -20, 50)
    window(leo, 15, -50, 50)
    window(leo, 65, -130, 50)
    window(leo, -30, -20, 50)
    window(leo, -80, -100, 50)
    window(leo, -80, -130, 50)
    rectangle(leo, -280, 100, 10, 1000)
    rectangle(leo, -255, 100, 10, 1000)
    rectangle(leo, -230, 100, 10, 1000)
    rectangle(leo, -205, 100, 10, 1000)
    rectangle(leo, -180, 100, 10, 1000)
    rectangle(leo, -155, 100, 10, 1000)
    rectangle(leo, -130, 100, 10, 1000)
    rectangle(leo, 145, 50, 30, 300)
    rectangle(leo, 185, 50, 30, 300)
    rectangle(leo, 225, 50, 30, 300)
    rectangle(leo, 265, 50, 30, 300)
    moon(leo, -250, 250, 40, 255, 255, 255)
    moon(leo, -230, 250, 30, 21, 34, 56)
    create_star(leo, -100, 200, 255, 251, 176)
    create_star(leo, 175, 250, 255, 251, 176)
    create_star(leo, 50, 183, 255, 251, 176)  
    create_star(leo, -50, 175, 255, 251, 176) 
    create_star(leo, 275, 150, 255, 251, 176) 
    done()


if __name__ == "__main__":
    main()