import turtle 
import random 
y_pos = -100
screen = turtle.Screen() 
screen.bgcolor("lightblue")

user = turtle.Turtle()
user.shape("turtle")
user.color("yellow")
user.penup()
user.goto(-200, 100)
user.speed(-10)

def move_right
x= user.xcor()
if  x <205:
    user.setx(x+20)
#keyboard events
screen.listen()
screen.onkey(move_right,"Right")

#create players
colors = ["blue", "green", "orange","purple"]

players = []

#postion and create players
for color in colors:
    player = turtle.Turtle(shape="turtle")
    player.color(color)
    
    player.penup()
    player.goto(-200, y_pos)

    player.append(player)
    y_pos += 50

#move players
def move_player():
    for players in players:
        distance = random.randint(1, 10)
        player.forward(distance)

# Game loop
game_over= False
while not game_over:
    moveplayers()
    for player in player:
        if player.xcor() >= 200:
            game_over= True
            if user.xcor() > player.xcor():
                winner = "red"
            else:
                winner= player.color()[0]
            break

# Display the winner
turtle.write(f"the {winner.upper()} turtle wins",
    align= "center",
    font=("Arial", 16, "bold"))
turtle.hideturtle()



turtle.done()
