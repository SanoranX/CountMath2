# -*- coding: utf-8 -*-

# Вычислительная математика лабораторная работа номер 2 (Python)
import matplotlib.pyplot as plt
import numpy as np


# Выполняем решение половинным делением
def halfDivisionMethod(x3, x2, x1, k, a, b, eps):
    if halfDivisionMethod_check(x3, x2, x1, k, a, b):
        return 0
    x = 0
    iteration_count = 0
    # Пока не достигнем нужной точности
    while abs(a - b) > eps:
        c = (a + b) / 2
        iteration_count += 1
        if f(a, x3, x2, x1, k) * f(c, x3, x2, x1, k) <= 0:
            b = c
        else:
            a = c
            x = (a + b) / 2
    return 'Ответ: ' + str(x) + ' & f(x) = ' + str(f(x, x3, x2, x1, k)) + ' & Количество итераций: ' + str(iteration_count)


# Проверка есть ли решения
def halfDivisionMethod_check(x3, x2, x1, k, a, b):
    return f(a, x3, x2, x1, k) * f(b, x3, x2, x1, k) > 0


# Решаем методом Ньютона
def newtonMethod(x3, x2, x1, k, end, eps):

    # Выбираем начальное приближение
    # f(x0) * f''(x0) > 0
    if f(leftBorderApprox, x3, x2, x1, k) * f2(leftBorderApprox, x3, x2) > 0:
        end = leftBorderApprox
    else:
        end = rightBorderApprox

    # Подсчет итераций
    iteration_count = 0

    # Вычисляем по формуле используя начальное приближение
    # Каждое следующее приближение корня рассчитывается на основании предшествующих данных
    tmp_1 = end
    tmp = tmp_1 # Приближение 1
    tmp_2 = tmp_1 - (f(tmp_1, x3, x2, x1, k) / f1(tmp_1, x3, x2, x1)) # x(iteration_count + 1) = f(xn) / f'(xn)

    # Продолжаем итерации, пока не достигнем заданной точности
    # Смотреть отчет с формулами, тут красиво не выйдет
    while abs(tmp - tmp_2) > eps:
        # Добавляем 1 к итерациям
        iteration_count += 1
        tmp = tmp_1
        tmp_1 = tmp_2
        # Расчитываем приближение
        tmp_2 = tmp - (f(tmp, x3, x2, x1, k) / f1(tmp, x3, x2, x1))
    return 'Ответ: ' + str(tmp) + ' & f(x) = ' + str(f(tmp, x3, x2, x1, k)) + ' & Количество итераций: ' + str(iteration_count)


# Решение способом простой итерации
def simpleIterationMethod(x3, x2, x1, k, a, b, eps):
    if simpleIterationMethod_check(a, b, k):
        return 0
    MIN_RANGE = a # Левая граница приближения
    MAX_RANGE = b # Правая граница приближения
    x = b
    iteration_count = 0
    x = searchX(MIN_RANGE, MAX_RANGE, x, x3, x2, x1)
    lambd = getLambda(x, x3, x2, x1)
    x0 = x
    x = x - lambd * (f(x, x3, x2, x1, k))
    while abs(x - x0) >= eps:
        x0 = x
        x = x - lambd * (f(x, x3, x2, x1, k))
        iteration_count += 1
    return 'Ответ: ' + str(x0) + ' & f(x) = ' + str(f(x0, x3, x2, x1, k)) + ' & Количество итераций: ' + str(iteration_count)


# Проверяем условие сходимости
def simpleIterationMethod_check(a, b, k):
    count_1 = 1 / (3 * pow(abs(a - k), -2 / 3)) if (a - k > 0) else 0
    count_2 = 1 / (3 * pow(abs(b - k), -2 / 3)) if (b - k > 0) else 0
    return count_1 >= 1 and count_2 >= 1


# Обычная f(x) функция
def f(x, x3, x2, x1, k):
    return x3 * pow(x, 3) + x2 * pow(x, 2) + x1 * x + k


# Первая производная
def f1(x, x3, x2, x1):
    return 3 * x3 * pow(x, 2) + 2 * x2 * x + x1


# Вторая производная
# См. производные
def f2(x, x3, x2):
    return 6 * x3 * x + 2 * x2


def searchX(min_range, max_range, x, x3, x2, x1):
    a = f1(min_range, x3, x2, x1)
    b = f1(max_range, x3, x2, x1)
    c = f1(x, x3, x2, x1)
    if a >= b and a >= c:
        return min_range
    else:
        if b >= a and b >= c:
            return max_range
        else:
            return x


def getLambda(x, x3, x2, x1):
    return 1 / (3 * x3 * pow(x, 2) - 2 * x2 * x - x1)


def printGraphFor5(a, b):
    fig, ax = plt.subplots()
    x = np.linspace(a, b, 1000)
    y2 = f(x, indexX3, indexX2, indexX1, indexK)
    ax.plot(x, y2)
    plt.show()


def printGraph(a, b):
    fig, ax = plt.subplots()
    x = np.linspace(a, b, 1000)
    y = f(x, indexX3, indexX2, indexX1, indexK)
    ax.plot(x, y)
    plt.show()

if __name__ == '__main__':
    isAnswered = True
    isEnteringManually = True
    print("Добро пожаловать! Следуйте, пожалуйста, инструкциям.")
    while isEnteringManually:
        print('[MENU]\n[1] - Для того, чтобы открыть из файла\n[2] - Для того, чтобы написать вручную')
        mes = input()
        if mes == "1":
            try:
                inputDocumentPath = open('input', 'r')
                indexX3, indexX2, indexX1, indexK = map(float, inputDocumentPath.readline().split(' '))
                leftBorderApprox, rightBorderApprox = map(float, inputDocumentPath.readline().split(' '))
                epsilon = float(inputDocumentPath.readline())

                isAnswered = True
                isEnteringManually = False
            finally:
                inputDocumentPath.close()
        # Спрашиваем у пользователя все коэффициэнты в случае, если вводится вручную
        if mes == "2":
            print('Введите, пожалуйста, коэффициент перед x^3: ')
            indexX3 = float(input())
            print('Введите, пожалуйста, коэффициент перед x^2: ')
            indexX2 = float(input())
            print('Введите, пожалуйста, коэффициент перед x^1: ')
            indexX1 = float(input())
            print('Введите, пожалуйста, свободный член: ')
            indexK = float(input())
            print('Введите, пожалуйста, левую границу приближения: ')
            leftBorderApprox = float(input())
            print('Введите, пожалуйста, правую границу приближения: ')
            rightBorderApprox = float(input())
            print('Введите, пожалуйста погрешность: ')
            epsilon = float(input())
            isAnswered = True
            isEnteringManually = False

    print('Выберите метод решения:\n1. Половинного деления\n2. Метод Ньютона\n3. Метод простой итерации\nВаш ответ: ')
    answer = ''

    while isAnswered:
        give = input()
        if give == '1':
            printGraph(leftBorderApprox, rightBorderApprox)
            answer = halfDivisionMethod(indexX3, indexX2, indexX1, indexK, leftBorderApprox, rightBorderApprox, epsilon)
            isAnswered = False
        elif give == '2':
            printGraph(leftBorderApprox, rightBorderApprox)
            answer = newtonMethod(indexX3, indexX2, indexX1, indexK, rightBorderApprox, epsilon)
            isAnswered = False
        elif give == '3':
            printGraphFor5(leftBorderApprox, rightBorderApprox)
            answer = simpleIterationMethod(indexX3, indexX2, indexX1, indexK, leftBorderApprox, rightBorderApprox, epsilon)
            isAnswered = False
        else:
            print('Ошибка: не тот номер \n' +
                  'попробуйте еще раз')
            continue

        print(answer)
        # Открываем файл, чтобы записать в него ответ
        try:
            with open('output.txt', 'w') as file:
                file.writelines(answer)
        except:
            print("[Ошибка]\nРешения отсутствуют")
        finally:
            file.close()
