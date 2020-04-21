print("Vamos somar os números que você digitar, não se esqueça de digitar 0 para parar e calculá-los!")
núm = cont = soma = 0
núm = int(input("Digite um número [0 para parar]: "))
while núm != 0:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [0 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}. ' .format(cont,soma))

print('Fim do programa')