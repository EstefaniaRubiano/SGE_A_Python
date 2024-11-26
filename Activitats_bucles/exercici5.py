#Copiar exercici anterior i modificar-lo per a que 
# mostri la suma dels números parells i la suma dels números imparells.

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

sumaParells = 0
sumaSenars = 0

for i in num:
    if i % 2 == 0:
        sumaParells += i
    else:
        sumaSenars += i

print(f"Suma dels números parells: {sumaParells}")
print(f"Suma dels números senars: {sumaSenars}")

