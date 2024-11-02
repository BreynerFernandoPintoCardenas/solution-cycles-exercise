def secuencia_collatz(n):
    secuencia = []
    while n != 1:
        secuencia.append(n)
        if n % 2 == 0:  
            n //= 2
        else:           
            n = 3 * n + 1
    secuencia.append(1)  
    return secuencia

def graficar_collatz(limite):
    for i in range(1, limite):
        secuencia = secuencia_collatz(i)
        largo = len(secuencia)
        print(f"{i} {'*' * largo}")

n = int(input("Ingrese un número entero positivo: "))


print(f"Secuencia de Collatz para n = {n}:")
print(" ".join(map(str, secuencia_collatz(n))))


print("\nLargos de las secuencias de Collatz:")
graficar_collatz(n)
