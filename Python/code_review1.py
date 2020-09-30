#Script: Number race
'''
    Description:
    randint:let you generate integer number
    uniform:let you generate float number
'''

import os
from random import randint

#Functions :::::::::::::::::::::::::::::::::::::::::
def dices () :
    d1 = randint(1,6)
    d2 = randint(1,6)
    tot = d1 + d2
    return [d1, d2, tot]

def lanzamientos () :
    # Valida solo numeros
    while True:
        try:
            L = int(input("Cuantos lanzamientos desea hacer: "))
            if L<1 :
                print('\nATENCIÓN: Debe ingresar un número entero mayor a 0.')
            else:
                n = L
                return n
        except:
            print('\nATENCIÓN: Debe ingresar un número entero mayor a 0.')
    return n

#Main ::::::::::::::::::::::::::::::::::::::::::::::
os.system("cls")
print("El minimo de lanzamientos aceptado es 1")
lan = lanzamientos()
i = 1
h = 0
P = 0
I = 0
while i <= lan:
    print("Tiro Nro: ", i)
    dd = dices()
    print("Dice1: ", dd[0])
    print("Dice2: ", dd[1])
    print("Total: ", dd[2])
    i += 1
    key = input("::: Lance Nuevamente :::")
    h += dd[2]
    if dd[2]%2 == 0:
        P += 1
    if dd[2]%2 != 0:
        I += 1
    if dd[2] == 12 or (i-1)  == lan:
        print("Sumatoria lanzamientos: ", h)
        print("Conteo de pares: ", P)
        print("Conteo de Impares: ", I)
        exit(0)
