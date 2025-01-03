import turtle
import random

# Drawing functions for different dishes
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_tiramisu(t):
    # Draw Tiramisu layers
    draw_rectangle(-150, 0, 300, 40, "saddlebrown")  # Bottom layer (chocolate)
    draw_rectangle(-150, 40, 300, 40, "wheat")  # Middle layer (coffee-soaked ladyfingers)
    draw_rectangle(-150, 80, 300, 40, "ivory")  # Top layer (mascarpone cream)

    # Add cocoa powder (small dots)
    t.penup()
    t.goto(-140, 120)
    t.setheading(0)
    t.pendown()
    t.pencolor("brown")
    for _ in range(10):
        t.dot(10, "brown")
        t.penup()
        t.forward(30)
        t.pendown()

def draw_pizza(t):
    # Function to draw a circle (for pizza base, cheese, and pepperoni)
    def draw_circle(x, y, radius, color):
        t.penup()
        t.goto(x, y - radius)  # Adjust the y-coordinate to center the circle
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    # Draw the pizza base (crust)
    draw_circle(0, 0, 150, "peru")

    # Draw the cheese layer
    draw_circle(0, 0, 130, "gold")

    # Add pepperoni slices
    pepperoni_positions = [
        (-50, 50), (50, 50), (-70, -40),
        (70, -40), (0, 70), (0, -70), (0, -10)
    ]

    for x, y in pepperoni_positions:
        draw_circle(x, y, 20, "red")

# Dictionary for recipes (case insensitive keys)
recipes = {
    "italian": {
        "tiramisu": {
            "ingredients": ["Ladyfingers", "Espresso", "Mascarpone cheese", "Sugar", "Cocoa powder", "Eggs", "Vanilla extract"],
            "steps": [
                "Dip ladyfingers in espresso and layer them in a dish.",
                "Mix mascarpone cheese, sugar, eggs, and vanilla extract until smooth.",
                "Spread the mascarpone mixture over the ladyfingers layer.",
                "Repeat the layers until the dish is filled.",
                "Dust with cocoa powder on top.",
                "Refrigerate for 4 hours before serving."
            ],
            "draw_function": draw_tiramisu
        },
        "pizza": {
            "ingredients": ["Pizza dough", "Tomato sauce", "Cheese", "Pepperoni slices",],
            "steps": [
                "Preheat the oven to 180°C",
                "Roll out the pizza dough and place it on a pizza tray or baking sheet.",
                "Spread a thin layer of tomato sauce on the dough.",
                "Top with shredded cheese and your choice of toppings (e.g., pepperoni, olives, bell peppers).",
                "Bake for 10-12 minutes until the crust is golden and the cheese is melted.",
                "Slice and enjoy!"
            ],
            "draw_function": draw_pizza  # Function for drawing a pizza
        }
    },
    "mexican": {
        "tacos": {
            "ingredients": ["Taco shells", "Ground beef", "Lettuce", "Tomatoes", "Cheese"],
            "steps": [
                "Cook the ground beef in a pan.",
                "Warm the taco shells in the oven.",
                "Fill each taco shell with beef, lettuce, tomatoes, and cheese."
            ],
            "draw_function": None  # No drawing function for tacos
        },
        "quesadillas": {
            "ingredients": ["Tortillas", "Cheese", "Chicken (optional)", "Bell peppers", "Onions"],
            "steps": [
                "Heat a pan over medium heat.",
                "Place a tortilla on the pan and sprinkle cheese evenly over one half.",
                "Add cooked chicken, bell peppers, and onions on top of the cheese (optional).",
                "Fold the tortilla in half and cook for 2-3 minutes on each side until golden and the cheese is melted.",
                "Slice into wedges and serve with salsa or sour cream."
            ],
            "draw_function": None  # No drawing function for quesadillas
        }
    }
}

# Main program
print("Welcome to the Recipe Generator!")

# Display available cuisines (in lower case for case-insensitive input)
print("Available cuisines:")
for cuisine in recipes.keys():
    print(f"- {cuisine.capitalize()}")

# Ask for the user's choice of cuisine (converting input to lower case for case-insensitive matching)
cuisine_choice = input("\nWhat type of cuisine would you like? ").lower()

# Check if the chosen cuisine exists (case-insensitive)
if cuisine_choice in recipes:
    # Display available dishes in the selected cuisine (convert dishes to lower case for input matching)
    print(f"\nDishes available in {cuisine_choice.capitalize()} cuisine:")
    for dish in recipes[cuisine_choice]:
        print(f"- {dish.capitalize()}")

    # Ask for the user's choice of dish (converting input to lower case for case-insensitive matching)
    dish_choice = input("\nWhich dish would you like? ").lower()

    # Check if the chosen dish exists (case-insensitive)
    if dish_choice in recipes[cuisine_choice]:
        chosen_recipe = recipes[cuisine_choice][dish_choice]

        # Display the recipe
        print("\nIngredients:")
        for ingredient in chosen_recipe["ingredients"]:
            print(f"- {ingredient}")
        
        print("\nSteps:")
        for step in chosen_recipe["steps"]:
            print(f"- {step}")

        # Ask the user if they want to see a drawing of thier dish
        draw_choice = input("\nWould you like to see a drawing of the dish? (yes/no) ").lower()
        if draw_choice == "yes":
            # Check if a drawing function is available
            if chosen_recipe["draw_function"] is not None:
                print("\nDrawing your dish...")
                screen = turtle.Screen()
                screen.title("Dish Drawing")
                screen.bgcolor("white")
                t = turtle.Turtle()
                t.speed(3)
                chosen_recipe["draw_function"](t)
                screen.mainloop()
            else:
                print("\nNo drawing available for this dish.")
        else:
            print("\nEnjoy your meal!")
    else:
        print("Sorry, that dish is not available.")
else:
    print("Sorry, that cuisine is not available.")
            
     
