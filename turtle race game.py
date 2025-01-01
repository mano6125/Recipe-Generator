import turtle
import random

def setup_race_track():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Turtle Race Game")
    
    # Draw race track
    track_drawer = turtle.Turtle()
    track_drawer.speed(0)
    track_drawer.penup()
    track_drawer.goto(-200, 100)
    
    for step in range(6):
        track_drawer.write(step * 50, align="center")
        track_drawer.right(90)
        track_drawer.pendown()
        track_drawer.forward(200)
        track_drawer.penup()
        track_drawer.backward(200)
        track_drawer.left(90)
        track_drawer.forward(50)
    track_drawer.hideturtle()

def create_turtle(color, y_position):
    t = turtle.Turtle()
    t.color(color)
    t.shape("turtle")
    t.penup()
    t.goto(-200, y_position)
    t.pendown()
    return t

def turtle_race():
    # Setup race track
    setup_race_track()

    # Create turtles
    colors = ["red", "blue", "green", "yellow", "purple"]
    turtles = []
    start_y = 80
    for color in colors:
        turtles.append(create_turtle(color, start_y))
        start_y -= 40

    # Start the race
    winner = None
    while not winner:
        for t in turtles:
            t.forward(random.randint(1, 10))  # Move forward by random steps
            if t.xcor() >= 200:  # Check if any turtle has crossed the finish line
                winner = t.color()[0]  # Get the winning turtle's color
                break

    # Announce the winner
    turtle.penup()
    turtle.goto(0, -100)
    turtle.hideturtle()
    turtle.color("black")
    turtle.write(f"The winner is the {winner} turtle!", align="center", font=("Arial", 16, "bold"))

# Run the game
turtle_race()
turtle.done()
