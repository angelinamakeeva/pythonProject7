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
        selected_colour = input("Пожалуйста,введите цвет:")
        if selected_colour.lower() == colour1 or selected_colour.lower() == colour2 or selected_colour.lower() == colour3 or selected_colour.lower() == colour4 or selected_colour.lower() == colour5 or selected_colour.lower() == colour6:
            print("Первый цвет выбран,", selected_colour)
            break
        else:
            print(selected_colour, "не является верным значением")

    while True:
        selected_colour2 = input("Пожалуйста,введите цвет:")
        if selected_colour2.lower() == colour1 or selected_colour2.lower() == colour2 or selected_colour2.lower() == colour3 or selected_colour2.lower() == colour4 or selected_colour2.lower() == colour5 or selected_colour2.lower() == colour6:
            if selected_colour2 != selected_colour:
                print("Второй цвет выбран,", selected_colour2)
                break
        else:
            print(selected_colour2, "не является верным значением")


def get_num_hexagon():
    while True:
        input_number = input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд:")
        if input_number.isdigit():
            number = int(input_number)
            if 4 <= number <= 20:
                print("Число принято:", number)
                break
            else:
                print("Оно должно быть от 4 до 20. Попробуйте еще раз.")
        else:
            print("Введено не число. Попробуйте еще раз.")

get_colour_choice()