import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("light blue")
screen.title("Birthday Cake")

# Create the turtle
artist = turtle.Turtle()
artist.speed(0)

# Function to draw a filled rectangle
def draw_rectangle(color, x, y, width, height):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.color(color)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(width)
        artist.left(90)
        artist.forward(height)
        artist.left(90)
    artist.end_fill()

# Function to draw a filled circle (used for candles and decorations)
def draw_circle(color, x, y, radius):
    artist.penup()
    artist.goto(x, y - radius)
    artist.pendown()
    artist.color(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

# Function to draw a candle
def draw_candle(x, y):
    # Candle body
    draw_rectangle("yellow", x, y, 10, 40)
    # Candle flame
    draw_circle("orange", x + 5, y + 40, 5)

# Function to draw the birthday cake
def draw_cake():
    # Bottom layer of the cake
    draw_rectangle("chocolate", -150, -100, 300, 50)

    # Middle layer of the cake
    draw_rectangle("pink", -120, -50, 240, 40)

    # Top layer of the cake
    draw_rectangle("light yellow", -90, -10, 180, 30)

    # Candles on the top layer
    candle_positions = [-60, -20, 20, 60]
    for pos in candle_positions:
        draw_candle(pos, 20)

    # Cake decorations
    for x in range(-140, 150, 30):  # Decorations for the bottom layer
        draw_circle("white", x, -110, 10)
    for x in range(-110, 120, 30):  # Decorations for the middle layer
        draw_circle("red", x, -60, 8)
    for x in range(-80, 100, 30):  # Decorations for the top layer
        draw_circle("blue", x, -20, 5)

# Draw the birthday cake
draw_cake()

# Hide the turtle
artist.hideturtle()

# Keep the window open
turtle.done()
 
