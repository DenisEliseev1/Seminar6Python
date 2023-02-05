# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


import math

def dist_2_point (a, b):
    sum = 0
    for i in range (n):
        sum = sum + (a[i]-b[i])**2
    sum = math.sqrt (sum)
    return round (sum,4)

try:
#    n = int (input ('Введите мерность пространства N='))
    n = 2
    p1 = input('Введите координаты точки 1 через пробел:')
    point1 = list(map(float,p1.split()))
    p2 = input('Введите координаты точки 2 через пробел:')
    point2 = list(map(float,p2.split()))
    print (p1, point1)
    print (f'расстоние от точки 1 до точки 2 - {dist_2_point (point1, point2)}')
except:
    print ('Не корректные значения: N - целое положительное число, координаты точек - любое число')


'''
Предыдущий код:
import math


def input_cord (n): #-УДАЛЕНА взамен -map-
    array = []
    for i in range (n):
        array.append (float (input (f'Введите координату {i+1} - ')))
    return array

def dist_2_point (a, b):
    sum = 0
    for i in range (n):
        sum = sum + (a[i]-b[i])**2
    sum = math.sqrt (sum)
    return round (sum,4)

try:
    n = int (input ('Введите мерность пространства N='))
    print ('Введите координаты точки 1:')
    point1 = input_cord (n)
    print ('Введите координаты точки 2:')
    point2 = input_cord (n)
    print (f'расстоние от точки 1 до точки 2 - {dist_2_point (point1, point2)}')
except:
    print ('Не корректные значения: N - целое положительное число, координаты точек - любое число')
'''