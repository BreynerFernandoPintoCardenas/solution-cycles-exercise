constante = 1
divisor = 1
fraccion = 0
suma = float(0)
i = 0

print("Potencia  Fraccion  Suma")
while True:  # Bucle infinito que se romperá con una condición
    i += 1
    divisor *= 2
    fraccion = constante / divisor
    suma += fraccion
    print(f"{i}         {fraccion:.6f}  {suma:.6f}")
    
    if fraccion <= 0.000001:  # Condición para terminar el bucle
        break