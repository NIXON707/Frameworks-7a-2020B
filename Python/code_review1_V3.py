import os
from random import randint

#----------Function print_dice----------------------------
def print_dice (dice_one, dice_two) :
    
    #---------Lists for the formation of the dice----------
    d1 = ['+-------+',
          '|       |',
          '|   O   |',
          '|       |',
          '+-------+']

    d2 = ['+-------+',
          '|     O |',
          '|       |',
          '| O     |',
          '+-------+']
    
    d3 = ['+-------+',
          '|     O |',
          '|   O   |',
          '| O     |',
          '+-------+']
        
    d4 = ['+-------+',
          '| O   O |',
          '|       |',
          '| O   O |',
          '+-------+']
        
    d5 = ['+-------+',
          '| O   O |',
          '|   O   |',
          '| O   O |',
          '+-------+']     
    
    d6 = ['+-------+',
          '| O   O |',
          '| O   O |',
          '| O   O |',
          '+-------+']
          
    dice = [d1, d2, d3, d4, d5, d6]
    #--END----Lists for the formation of the dice------
    
    d1 = dice[dice_one-1]
    d2 = dice[dice_two-1]
    res_dice = []
    
    #-----------combine dice--------
    for i in range(0,5):
        res_dice.append(d1[i]+d2[i])
        i += 1
    #---END-----combine dice-------    
    
    #----------Print two dice------    
    i = 0      
    res = ''      
    for ls in res_dice:
        for t in ls:
            if i == len(ls)/2: res += '   '
            res +=t
            i += 1
        print(res)
        res = ''
        i = 0
    #---END----Print two dice------
#--END-----Function print_dice------------------

#------Your roll two dice, and their sum--------
def dices1 () :
    player_dice_one = randint(1,6)               
    player_dice_two = randint(1,6)
    player_scope = player_dice_one + player_dice_two
    return [player_dice_one, player_dice_two, player_scope]

#------Your roll two dice, and their sum--------
def dices2 () :
    comp_dice_one = randint(1,6)
    comp_dice_two = randint(1,6)
    comp_scope = comp_dice_one + comp_dice_two
    return [comp_dice_one, comp_dice_two, comp_scope]

#------------release validator------------------
def lanzamientos () :
    # Valida solo numeros enteros > a 0.
    while True:
        try:
            L = int(input("Cuantos lanzamientos desea hacer: "))
            if L<1 :
                print('\nATENCIÓN: Debe ingresar un número entero mayor a 0.')
            else:
                return L
        except:
            print('\nATENCIÓN: Debe ingresar un número entero mayor a 0.')
    return L
#--END-------release validator------------------

#----------------level selection----------------
def nivel () :
    while True:
        try:
            L = int(input("\nSeleccionar el Nivel de la Competencia: "))
            if L<1 or L>3 :
                print('\nATENCIÓN: Debe ingresar un número entero entre 1 y 3.')
            elif L == 1:
                return 50
            elif L == 2:
                return 70
            else:
                return 100
        except:
            print('\nATENCIÓN: Debe ingresar un número entero entre 1 y 3.')
    return 
#--END-----------level selection----------------

#---------Determine the winner------------------
def winner (jugador1, jugador2) :
    if jugador1 > jugador2:
        print("\n----------"+ name1+ " GANA----------")
        print("\t!!! FELICITACIONES ¡¡¡")
    elif jugador1 < jugador2:
        print("\n----------"+ name2+ " GANA-----------")
        print("\t!!! FELICITACIONES ¡¡¡")
    else:
        print('--------Draw---------')
#---END---Determine the winner------------------

#---------Print result--------------------------

#Main ::::::::::::::::::::::::::::::::::::::::::::::

os.system("cls")
#print("\t\t\t!!! HOLA JUGADORES ¡¡¡\n\t\tSean bienvenidos a \"La Carrera Numerica\"")
print("\t\t\t!!! HOLA JUGADORES ¡¡¡\n\t\tSean bienvenidos a \"La Carrera Numerica\"\n\nHay 3 niveles el primero en llegar GANA")
print("\nNiveles Disponibles:\n[1.] Nivel básico (50 posiciones).\n[2.] Nivel intermedio (70 posiciones).\n[3.] Nivel avanzado (100 posiciones).")
name1 = input("\nJugador 1 ingresa tu nombre: ")
name2 = input("\nJugador 2 ingresa tu nombre: ")
lvl = nivel()
#print("\nEl minimo de lanzamientos aceptado es 1")
#lan = lanzamientos()

i = 1
h1 = 0; h2 = 0
P1 = 0; P2 = 0
I1 = 0; I2 = 0
while i :#<= lan :
    print("\nTiro N°: ", i)
    input("::: "+ name1+ " Lanza :::")
    dd1 = dices1()
    print("\n......"+ name1+ " Obtuviste......")    
    print_dice(dd1[0], dd1[1])
    print("Dice1: ", dd1[0], "   Dice2: ", dd1[1])
    print("Total: ", dd1[2])
    #//////////////////////////////////////////
    input("\n::: "+ name2+ " Lanza :::")
    dd2 = dices2()
    print("\n......"+ name2+ " Obtuviste......")    
    print_dice(dd2[0], dd2[1])
    print("Dice1: ", dd2[0], "   Dice2: ", dd2[1])
    print("Total: ", dd2[2])
    i += 1
    h1 += dd1[2]; h2 += dd2[2]
    if dd1[2] % 2 == 0:
        P1 += 1
    #else:
    #    I1 += 1
    #---------------------
    #elif dd1[2] % 2 != 0:
    #    I1 += 1
    #---------------------
    if dd1[2] % 2 != 0:
        I1 += 1
    if dd2[2] % 2 == 0:
        P2 += 1
    if dd2[2] % 2 != 0:
        I2 += 1
    '''
    if dd1[2] == 12 or dd2[2] == 12:# or (i-1)  == lan:
        print("\nLos resultados del Juagador 1 son:")
        print("Sumatoria lanzamientos: ", h1)
        print("Conteo de pares: ", P1)
        print("Conteo de Impares: ", I1)
        print("\nLos resultados del Juagador 2 son:")
        print("Sumatoria lanzamientos: ", h2)
        print("Conteo de pares: ", P2)
        print("Conteo de Impares: ", I2)
        winner(h1, h2)
        exit(0) '''
    if h1 == lvl or h2 == lvl:
        print("\nLos resultados de ", name1, " son:")
        print("Sumatoria lanzamientos: ", h1)
        print("Conteo de pares: ", P1)
        print("Conteo de Impares: ", I1)
        print("\nLos resultados de ", name2, " son:")
        print("Sumatoria lanzamientos: ", h2)
        print("Conteo de pares: ", P2)
        print("Conteo de Impares: ", I2)
        winner(h1, h2)
        exit(0)
    elif h1 >lvl:
        h1 = -dd1[2]
    elif h2 >lvl:
        h2 = -dd2[2]

#===============================================
