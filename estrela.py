num = int(input("Digite um número:"))

if num > 50:
    print("O número é fora dos limites!")
    print("Exibindo o tamanho máximo")
    num = 50
    input()
contador = 1
while contador <= num:
    print(contador * "*")
    contador = contador + 1