def calcular_tiempo_viaje():
    tiempo_total = 0

    while True:
        duracion_tramo = int(input("Duracion tramo: "))
        
        if duracion_tramo == 0:
            break
            
        tiempo_total += duracion_tramo

    # Convertir el tiempo total a horas y minutos
    horas = tiempo_total // 60
    minutos = tiempo_total % 60

    print(f"Tiempo total de viaje: {horas}:{minutos:02d} horas")

# Llamar a la función
calcular_tiempo_viaje()
