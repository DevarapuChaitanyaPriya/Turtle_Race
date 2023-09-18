import random
from turtle import Turtle, Screen

# Create a screen object
my_screen = Screen()
my_screen.setup(width=500, height=500)
my_screen.title('Turtle Race')
# Create a Turtle object for drawing the finish line
potti = Turtle()
potti.hideturtle()
potti.penup()
potti.goto(x=225, y=225)
potti.pendown()
potti.right(90)
potti.pencolor('green')
potti.forward(400)

# Ask the user to guess which turtle will win
user_input = my_screen.textinput("Who will win the race?(Red or Orange or Blue)", "Guess")


# Function to make a turtle move forward by a random distance
def race(obj):
    obj.forward(random.randint(1, 5))


# Define starting positions and colors for the turtle contestants
y_position = [0, -50, 50]
colors = ["red", "orange", "blue"]
contestants = []

# Create three turtle contestants
for i in range(3):
    tim = Turtle()
    tim.shape('turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(-235, y_position[i])
    contestants.append(tim)

# Check if the user made a guess
if user_input:
    again = True

# Start the race
while again:
    for i in contestants:
        if i.xcor() >= 225:
            again = False
            winner = i.pencolor()
            if winner == user_input.lower():
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")

    # Make a random contestant move forward
    race(random.choice(contestants))

# Set the screen title and exit on click
my_screen.title("Turtle Race")
my_screen = Screen()
my_screen.setup(width=500, height=500)
my_screen.exitonclick()
