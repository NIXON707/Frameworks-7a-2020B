#Este codigo muestra el Factorial del numero ingresado
#Estudiantes: Fabian Bedoya, Nixon Moncayo

import os
#N°1 CODIGO while ==============================

#Variables + solisitud a usuario :::::::::::::::::::::::::::::::::::::::::

os.system("cls")
num = int(input("Digite un número entero positivo mayor a cero: "))

factor = 1
cont = 1

#Ciclo :::::::::::::::::::::::::::::::::::::::::

while cont <= num :
    factor = factor * cont
    cont += 1

print(factor)
salto = input("\n\nPresione \'enter\' para ejecutar el segundo codigo")

#N°2 CODIGO for ==============================

#Variables + solisitud a usuario :::::::::::::::::::::::::::::::::::::::::

numero = int(input("\nDigite un número entero positivo mayor a cero: "))

fact = 1

if numero >= 0 :
    for i in range(1, numero+1) :
        fact = fact*i
    print(fact)