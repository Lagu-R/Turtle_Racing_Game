 from turtle import Turtle, Screen
 import random
 
 # variable for Turtle and Screen , from turtle module
 screen = Screen()
 screen.setup(width=500, height=400)
 # ask user which player will win
 user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
 #color
 collors = ('purple', 'blue', 'green', 'yellow', 'orange', 'red')
 x_pos = -230
 y_pos = -100
 all_turtles = []
 for i in collors:
     new_turtle = Turtle(shape="turtle")
     new_turtle.penup()
     new_turtle.goto(x= x_pos, y= y_pos)
     new_turtle.color(i)
     y_pos += 30
     all_turtles.append(new_turtle)
     
 if user_bet:
     is_race_on = True
 
 while is_race_on:
     for i in all_turtles:
         if i.xcor() > 230:
             is_race_on = False
             winner = i.pencolor()
             if winner == user_bet:
                 print("You Win! Congrats!")
             else:
                 print("You lost :( !")
             print(f"Winner color is {i.pencolor()}")
         else:
             rand_distance = random.randint(0, 10)
             i.forward(rand_distance)
     
 
 
 screen.exitonclick()
