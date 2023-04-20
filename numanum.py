numero_1 = int(input("Digite o primeiro número:"))
numero_2 = int(input("Digite o segundo número:"))

if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1

contadora = numero_1
while contadora <= numero_2:
    print(contadora)
    contadora = contadora + 1