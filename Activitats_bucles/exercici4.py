<<<<<<< HEAD
#Imprimir els números parells i els imparells continguts en la següent llista. 
# Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

parells = ""
senars = ""

for i in num:
    if i % 2 == 0:
        parells += f"{i} "
    else:
        senars += f"{i} "

print(f"Números parells: {parells}")
print(f"Números senars: {senars}")

=======
#Imprimir els números parells i els imparells continguts en la següent llista. 
# Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

parells = ""
senars = ""

for i in num:
    if i % 2 == 0:
        parells += f"{i} "
    else:
        senars += f"{i} "

print(f"Números parells: {parells}")
print(f"Números senars: {senars}")

>>>>>>> 65685645d65cd72a2684ea997ae661b179101cd5
    