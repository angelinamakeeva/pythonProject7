import turtle
def get_colour_choice():
    colour1 = "розовый"
    colour2 = "голубой"
    colour3 = "синий"
    colour4 = "фиолетовый"
    colour5 = "желтый"
    colour6 = "зеленый"
    print("Допустимые цвета заливки:")
    print("*",colour1)
    print("*",colour2)
    print("*",colour3)
    print("*",colour4)
    print("*",colour5)
    print("*",colour6)
    while True:
        selected_colour = input("Пожалуйста, введите первый цвет:")
        if selected_colour.lower() == colour1 or selected_colour.lower() == colour2 or selected_colour.lower() == colour3 or selected_colour.lower() == colour4 or selected_colour.lower() == colour5 or selected_colour.lower() == colour6:
            return selected_colour
    else:
            print(selected_colour, "не является верным значением")

    while True:
        selected_colour2 = input("Пожалуйста,введите второй цвет:")
        if selected_colour2.lower() == colour1 or selected_colour2.lower() == colour2 or selected_colour2.lower() == colour3 or selected_colour2.lower() == colour4 or selected_colour2.lower() == colour5 or selected_colour2.lower() == colour6:
            if selected_colour2 != selected_colour:
                return selected_colour2
        else:
            print(selected_colour2, "не является верным значением")


def get_num_hexagon():
    while True:
        input_number = input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ")
        if input_number.isdigit():
            number = int(input_number)
            if 4 <= number <= 20:
                print("Число принято:", number)
                break
            else:
                print("Оно должно быть от 4 до 20. Попробуйте еще раз.")
        else:
            print("Введено не число. Попробуйте еще раз.")

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
    turtle.end_fill()

turtle.speed(10)
draw_hexagon(0, 0, 100, "black" )
turtle.done()

get_colour_choice()
get_num_hexagon()
