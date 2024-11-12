#Aplicar IVA segons el salari: s'aplica el IVA (0,10,21) segons el salari indicat. Si és menor de 15000, s'aplica un 0%.
#Si és menor de 30000 s'aplica un 10% i si és menor a 60000 s'aplica un 21%.

salari = 5000

if salari < 15000:
    iva = 0

elif salari < 30000:
    iva = 10

elif salari < 60000:
    iva = 21

calcul_iva = salari * iva / 100
