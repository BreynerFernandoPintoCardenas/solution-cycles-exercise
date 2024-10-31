cantidad=int(input("ingrese la cantidad de tramos que realizo: "))
timpoT=0
for i in range(cantidad):
    tramo=float(input("ingrese la duracion del tramo: "))
    timpoT+=tramo

horas=int(timpoT//60)
minutos=int(timpoT%60)

print(f"el tiempo total de tu recorrido fue de {horas}:{minutos} horas")