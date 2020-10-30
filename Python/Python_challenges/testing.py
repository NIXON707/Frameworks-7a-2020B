#Inicio del programa
contador = 0
acumulador = 0
x = 1
m3 = 0
m5 = 0
limite = 1000

while x <= limite :
    contador = contador + 1
    if contador % 3 == 0 :
        m3 = m3 + contador
    else :
        if contador % 5 == 0 :
            m5 = m5 + 1
    acumulador = acumulador + x
    x = x + 1
print(m5)
#Fin del programa

