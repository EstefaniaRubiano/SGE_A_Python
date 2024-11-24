#Amb while indicar si el número guardat a una variable 
# està entre 100 i 400.

num = int(input("Digues un número: "))

while num >= 0:
    if 100 <= num <= 400:
        print(f"El número {num} està entre 100 i 400")
    else:
        print(f"El número {num} no està entre 100 i 400")
    num = int(input("Digues un número: "))

    
    