for j in range(1, 11):
    print(f"{j:2}", end=" ")  

for i in range(1, 11):
    
    print(f"{i:2}", end=" ")  
    
    for j in range(1, 11):
        value = i * j  
        print(f"{value:2}", end=" ")  
    
    print() 

