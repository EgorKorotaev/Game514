# импорт необходимых пакетов

import time

import sys

import os


# Функция для реализации анимации загрузки

def load_animation():
    # Строка, которая будет отображаться при загрузке приложения

    load_str = "starting your console application..."

    ls_len = len(load_str)

    # Строка для создания вращающейся линии

    animation = "|/-\\"

    anicount = 0

    # используется для отслеживания

    # продолжительность анимации

    counttime = 0

    # указатель для перемещения строки загрузки

    i = 0

    while (counttime != 100):

        # используется для изменения скорости анимации

        # чем меньше значение, тем быстрее будет анимация

        time.sleep(0.075)

        # преобразование строки в список

        # как строка неизменна

        load_str_list = list(load_str)

        # x-> получение кода ASCII

        x = ord(load_str_list[i])

        # y-> для хранения измененного кода ASCII

        y = 0

        # если символ "." или "", оставьте его без изменений

        # переключать прописные буквы в строчные и наоборот

        if x != 32 and x != 46:

            if x > 90:

                y = x - 32

            else:

                y = x + 32

            load_str_list[i] = chr(y)

        # для хранения результирующей строки

        res = ''

        for j in range(ls_len):
            res = res + load_str_list[j]

        # отображение результирующей строки

        sys.stdout.write("\r" + res + animation[anicount])

        sys.stdout.flush()

        # Назначение строки загрузки

        # к результирующей строке

        load_str = res

        anicount = (anicount + 1) % 4

        i = (i + 1) % ls_len

        counttime = counttime + 1

    # для ОС Windows

    if os.name == "nt":

        os.system("cls")



    # для Linux / Mac OS

    else:

        os.system("clear")


# Драйверная программа

if __name__ == '__main__':
    load_animation()

    # Ваш нужный код продолжается здесь

    # s = input ("Введите ваше имя:")

    s = "David"

    sys.stdout.write("Hello " + str(s) + "\n")