def dibujar_hexagono(tamano):

​    

​    for i in range(tamano):

​        espacios = ' ' * (tamano - i - 1)

​        asteriscos = '*' * (1 * tamano + 2 * i)

​        print(espacios + asteriscos)

​    

​    

​    for i in range(tamano - 1, 0, -1):

​        espacios = ' ' * (tamano - i)

​        asteriscos = '*' * (1 * tamano + 2 * (i - 1))

​        print(espacios + asteriscos)

lado = int(input("Lado: "))

dibujar_hexagono(lado)