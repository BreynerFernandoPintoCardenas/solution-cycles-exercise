while diferencia >= 0.0001:
    factorial = math.factorial(n)
    
    # Sumar el término 1/n! a euler
    euler += 1 / factorial
    
    if n > 0:  # No calculamos diferencia para n=0
        diferencia = abs(1 / factorial - prev_term)
    
    prev_term = 1 / factorial  # Guardar el término actual
    
    n += 1

print(f"Valor aproximado de e: {euler}")