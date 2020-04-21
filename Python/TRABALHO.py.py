print('='*40)
print('{:^40}'.format('BANCO DO SAULLO'))
print('='*40)
valor = int(input('Qual valor você quer sacar? R$'))
notas = [50, 20, 10]
for nota in notas:
    ced = valor // nota
    if ced > 0:
        print(f'Total de {ced} cédulas de R${nota}')
    valor = valor - ced * nota
print('='*40 + '\nVolte sempre ao BANCO DO SAULLO! Tenha um bom dia!')