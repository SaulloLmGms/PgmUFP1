print("Vamos descobrir quais são os números pares até o que você digitar?!")

fim = int(input("Digite o último número a imprimir: "))
x = 1
while x <= fim:
     if x % 2 == 0:
         print(x)
     x = x + 1

print("Fim do programa!")