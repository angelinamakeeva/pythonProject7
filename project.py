#Osokina Anastasya 85%
#Kareva Alena 95%
#Makeeva Angelina 70%

import ru_local as ru
import turtle
import math

def get_colour_choice():
    color = ru.LST_COLOR
    while True:
        print(ru.VR_COLOR)
        select_color_1 = input(ru.PLS_COLOR)
        if select_color_1 in color:
            print(ru.FIRST_COLOR, select_color_1)
            break
        else:
            print(select_color_1, ru.NOT_VALUE)

    while True:
        print(ru.VR_COLOR)
        select_color_2 = input(ru.PLS_COLOR)
        if select_color_2 in color:
            print(ru.SECOND_COLOR, select_color_2)
            break
        else:
            print(select_color_2, ru.NOT_VALUE)
    
    dictionary = {
        ru.PINK : 'pink',
        ru.CYAN : 'cyan',
        ru.BLUE : 'blue',
        ru.PURPLE : 'purple',
        ru.YELLOW : 'yellow',
        ru.GREEN : 'green'
    }

    return dictionary[select_color_1], dictionary[select_color_2]

def get_num_hexagon():
    while True:
        input_number = input(ru.PLS_NUM)
        if input_number.isdigit():
            number = int(input_number)
            if 4 <= number <= 20:
                print(ru.NUM, number)
                break
            else:
                print(ru.EXSEPT)
        else:
            print(ru.NOT_INT)
    return input_number


def draw_hexagon(x, y, side_len, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(90)
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)
    turtle.left(90)
    turtle.end_fill()

color1, color2 = get_colour_choice()
number_hexagons = int(get_num_hexagon())

x = -250
y = 250
little_diagonal = 500 // number_hexagons
side_len = little_diagonal / 3 ** 0.5
x += side_len / 2
y -= little_diagonal / 2

for row in range(number_hexagons):
    for columns in range(number_hexagons):
        if (row + columns) % 2 == 0:
            draw_hexagon(x + columns * (math.sqrt(3 * side_len * side_len)), y - row * (side_len * 1.5), side_len, color1)
        else:
            draw_hexagon(x + columns * (math.sqrt(3 * side_len * side_len)), y - row * (side_len * 1.5), side_len, color2)
    if row % 2 == 0:
        x -= (math.sqrt(3 * side_len * side_len)) / 2
    else:
        x += (math.sqrt(3 * side_len * side_len)) / 2

turtle.speed(100)
turtle.mainloop()
