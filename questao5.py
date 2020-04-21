numero = int(input("Digite um número: "))
freio = 0
l = []

while numero != freio:
    l.append(numero)
    numero = int(input("Digite um número: "))

desejado = int(input("Digite o número: que deseja consultar: "))

if l.count(desejado) == 1:
    print("O Número",desejado, "aparece", l.count(desejado), "vez.")
else:
    print("O Número",desejado, "aparece", l.count(desejado), "vezes.")

print("FIM!")