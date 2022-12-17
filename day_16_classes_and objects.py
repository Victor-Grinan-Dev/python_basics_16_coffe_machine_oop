# day 16 - "Object oriented programing (OOP) the coffee machine again :)"

# CLASS NOTES:
# from turtle import Turtle, Screen
#
# timy = Turtle()
# timy.shape("turtle")
# timy.color("coral")
# timy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import *

my_table = PrettyTable()
my_table.add_column("pokemon name", ["picachu", "squirtle", "charmander"])
my_table.add_column("type", ["electric", "water", "fire"])

my_table.align = "c"  # l or r

print(my_table)
