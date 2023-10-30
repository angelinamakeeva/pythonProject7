#Osokina Anastasya 85%
#Kareva Alena 
#Makeeva Angelina 

import turtle
import math

def get_colour_choice():
    color = ['розовый', 'голубой', 'синий', 'фиолетовый', 'желтый', 'зеленый']
    while True:
        print('Допустимые цвета заливки: розовый, голубой, синий, фиолетовый, желтый, зеленый')
        select_color_1 = input('Пожалуйста, введите цвет: ')
        if select_color_1 in color:
            print('Первый вет выбран: ', select_color_1)
            break
        else:
            print(select_color_1, "не является верным значением")

    while True:
        print('Допустимые цвета заливки: розовый, голубой, синий, фиолетовый, желтый, зеленый')
        select_color_2 = input('Пожалуйста, введите цвет: ')
        if select_color_2 in color:
            print('Второй цвет выбран: ', select_color_2)
            break
        else:
            print(select_color_2, "не является верным значением")
    
    dictionary = {
        'розовый' : 'pink',
        'голубой' : 'cyan',
        'синий' : 'blue',
        'фиолетовый' : 'purple',
        'желтый' : 'yellow',
        'зеленый' : 'green'
    }

    return dictionary[select_color_1], dictionary[select_color_2]

def get_num_hexagon():
    while True:
        input_number = input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд:")
        if input_number.isdigit():
            number = int(input_number)
            if 4 <= number <= 20:
                print("Число принято: ", number)
                break
            else:
                print("Оно должно быть от 4 до 20. Попробуйте еще раз.")
        else:
            print("Введено не число. Попробуйте еще раз.")
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