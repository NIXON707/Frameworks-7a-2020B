#Este codigo solisita varios numeros hasta que la suma de los ya ingresados sea mayor a 100
#Estudiantes: Fabian Bedoya, Nixon Moncayo

import os

#Variables + solisitud a usuario :::::::::::::::::::::::::::::::::::::::::

os.system("cls")
print("Digite varios números individualente hasta que la suma de los mismos sea mayor a 100")

#Variables + solisitud a usuario :::::::::::::::::::::::::::::::::::::::::



#Functions :::::::::::::::::::::::::::::::::::::::::

def solicitud () :
    ct3 = 0
    ct2 = 0
    ent = int(input())
    if ent == 3 :
        ct3 += 1
    elif ent == 2 :
        ct2 += 1
    return [ent, ct2, ct3]

#::::END Functions

suma = 0
num = solicitud()

while True :
    try:
        if num[2] > 3 :
            print("No puede volver a digitar el número 3")
        elif num[1] > 2 :
            print("No puede volver a digitar el número 2")
    except:
        print(solicitud())
        
    if suma <= 100 :
        print("\nDigite el numero a ingresar:")
        suma = suma + num[0]
    
print("\nLa suma de sus numeros es: "+str(suma))
