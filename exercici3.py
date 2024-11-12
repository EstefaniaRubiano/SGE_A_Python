#Nota Mòdul: es mira la nota i segons la nota sortirà per pantalla la nota (S,A,N,E)

nota = 8.5

if 0 <= nota <= 4.99:
    print("L'alumne ha suspès.")

elif 5 <= nota <= 6.5:
    print("L'alumne ha aprovat")

elif 6.6 <= nota <= 8:
    print("L'alumne ha tret notable.")

elif nota > 8:
    print("L'alumne ha tret excelent.")