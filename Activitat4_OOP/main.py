# Importar les classes des dels arxius
from cotxe import Cotxe 
from colibri import Colibri 

# Crear les tres instàncies de Cotxe
cotxe1 = Cotxe("Tesla", "Model 2", 2021, "Negre", 50000)
cotxe2 = Cotxe("Toyota","Corolla", 2020, "Blau", 30000)
cotxe3 = Cotxe("Ford", "Fiesta", 2019, "Vermell", 20000)

# Crear les tres instàncies de Colibri
colibri1 = Colibri("Emperador", "Blau", 3, 40, 5)
colibri2 = Colibri("Rubí", "Verd", 2, 30, 4)
colibri3 = Colibri("Gorgeta", "Groc", 1, 35, 3.5)

# Mostrar 3 getters de Cotxe
print(f'Cotxe1, Marca: {cotxe1.getMarca()}') 
print(f'Cotxe2, Model: {cotxe2.getModel()}')
print(f'Cotxe3, Any de fabricació: {cotxe3.getAny_fabricació()}')

# Mostrar 4 getters de Colibri
print(f'Colibri1, Espècie: {colibri1.getEspecie()}')
print(f'Colibri2, Color: {colibri2.getColor()}')
print(f'Colibri3, Velocitat: {colibri3.getVelocitat()}')
print(f'Colibri1, Pes: {colibri1.getPes()}')

# Modificar 2 atributs de Cotxe (setters) i després mostrar-los (getters)
cotxe1.setColor("Gris")
cotxe2.setPreu(16000)
print(f'Cotxe1, Color modificat: {cotxe1.getColor()}')
print(f'Cotxe2, Preu modificat: {cotxe2.getPreu()}')

# Modificar 2 atributs de Colibri (setters) i després mostrar-los (getters)
colibri1.setColor("Rosa")
colibri2.setVelocitat(45)
print(f'Colibri1, Color modificat: {colibri1.getColor()}')
print(f'Colibri2, Velocitat modificada: {colibri2.getVelocitat()}')
