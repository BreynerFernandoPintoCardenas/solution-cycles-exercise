# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número: "))

# Inicializar una lista para almacenar los divisores
divisores = []

# Iterar desde 1 hasta el número ingresado (inclusive)
for i in range(1, numero + 1):
    if numero % i == 0:  # Comprobar si 'i' es un divisor de 'numero'
        divisores.append(i)  # Agregar 'i' a la lista de divisores

# Imprimir los divisores
print("Los divisores son:", " ".join(map(str, divisores)))
