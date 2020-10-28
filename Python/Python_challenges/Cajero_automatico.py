#Este codigo muestra el Factorial del numero ingresado
#Estudiantes: Fabian Bedoya, Nixon Moncayo

import os

#------------------Functions----------------------------

def dinero(cantidad, tipo):
    monedas = cantidad // tipo
    resto = cantidad % tipo

    return monedas, resto


def imprime_cambio(cantidad, nombre, tipo):
    if cantidad > 0:
        cadena = ('{0} de {1}.\n'.format(nombre, tipo))*cantidad
        print(cadena)

#---------------End Functions---------------------------

os.system("cls")

#Variables + solisitude to user :::::::::::::::::::::::::::::::::::::::::
print('\t\t::: RETIROS EN EFECTIVO :::')
try:
    monto = int(input('\n.: Diqite e1 valor a retirar ($): '))
    print()

    mon100, resto = dinero(monto, 100)
    mon50, resto = dinero(resto, 50)
    mon20, resto = dinero(resto, 20)
    mon10, resto = dinero(resto, 10)
    mon5, resto = dinero(resto, 5)
    mon1, resto = dinero(resto, 1)

    imprime_cambio(mon100, "moneda", 100)
    imprime_cambio(mon50, "moneda", 50)
    imprime_cambio(mon20, "moneda", 20)
    imprime_cambio(mon10, "moneda", 10)
    imprime_cambio(mon5, "moneda", 5)
    imprime_cambio(mon1, "moneda", 1)

except:
    print('El valor introducido no es valido.')

