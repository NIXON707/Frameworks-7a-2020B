#Estos codigos muestran la cantidad de numeros solicitada de la serie Fibonacci
#Estudiantes: Fabian Bedoya, Nixon Moncayo

#N°1 CODIGO SIMPLE ==============================

import os

#Variables + solisitud a usuario :::::::::::::::::::::::::::::::::::::::::

os.system("cls")

ent = int(input("Ingrese la cantidad de numeros que desea visualizar: "))

cont = 3
suma = 0
num1, num2 = 0, 1

#Proseso de  generación :::::::::::::::::::::::::::::::::::::::::

print("\nSecuencia completa: ")
print(num1, '', num2, ' ', end='')
while cont <= ent :
    suma = num1+num2
    print(suma, ' ', end='')
    num1, num2 = num2, suma
    cont +=1

salto = input("\n\nPresione \'enter\' para ejecutar el segundo codigo")

#N°2 CODIGO CON FORMULA MATEMATICA ==============================

#Formula para secuencia Fibonacci, a= Numero áureo (Numero de oro)

#   (a)^n - (-1/a)^n  |      1+(5)**0.5
#   ----------------  |  a = ----------
#       (5)**0.5      |          2

#Solisitud a usuario :::::::::::::::::::::::::::::::::::::::::

entra = int(input("\nIngrese la cantidad de numeros que desea visualizar: "))
entra = entra - 1

#Functions :::::::::::::::::::::::::::::::::::::::::

def oro(entra) :
    a = (1+(5)**0.5)/2
    return round(((a**entra)-(-1/a)**entra)/(5)**0.5)

print("\nEl ultimo termino de la secuencia Fibonacci para "+ str(entra + 1) + " es: " + str(oro(entra))+"\n")

#Variables + Ciclo :::::::::::::::::::::::::::::::::::::::::

cnt = 0
serie = []

while entra >= cnt :
    serie.append(oro(entra-cnt))
    cnt += 1
    
print("Secuencia completa: " + str(sorted(serie)))