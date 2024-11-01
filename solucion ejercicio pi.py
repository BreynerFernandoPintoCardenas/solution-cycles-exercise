n = int(input("Ingrese un número entero n: "))

pi = 0

divisor = 1

for i in range(n):

​    

​    if i % 2 == 0:

​        pi += 4 / divisor 

​        

​    else:

​        pi -= 4 / divisor  

​        

​    

​    divisor += 2

print(pi)