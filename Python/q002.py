print("Digite um número e iremos saber seu respectivo fatorial! ")

numero = int(input("Fatorial de: "))
resultado = 1
count = 1
while count <= numero:
    resultado *= count
    count += 1
print("O fatorial de" , numero, "é" , resultado)

print('Fim do programa! ')