#Verificar maior e menor da lista

valores = []
for cont in range(0, 5):
    valores.append(int(input('DIGITE UM VALOR: ')))

print(f'VOCÊ DIGITOU OS VALORES {valores}')
print(f'O MAIOR VALOR FOI {max(valores)} NA POSIÇÃO {valores.index(max(valores))}')
print(f'O MENOR VALOR FOI {min(valores)} NA POSIÇÃO {valores.index(min(valores))}')

print("FIM!")