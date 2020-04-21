#Remover numero repetido.

numero = int(input("Digite um número: "))
freio = 0
l = []

while numero != freio:
    l.append(numero)
    numero = int(input("Digite um número: "))
    l.count(numero)
    if numero in l:
        l.remove(numero)

print(l)

print("FIM!")