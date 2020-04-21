print('='*30)
print('{:^30}'.format('BANCO DO SAULLO '))
print('='*30)
valor = ced5 = ced50 = ced20 = ced10 = ced100 = 0
valor = int(input('Qual valor que você quer sacar? R$'))
while valor >= 100:
    valor -= 100
    ced100 += 1
while valor >= 50:
    valor -= 50
    ced50 += 1
while valor >= 20:
    valor -= 20
    ced20 += 1
while valor >= 10:
    valor -= 10
    ced10 += 1
while valor >= 5:
    valor -= 5
    ced5 += 1
if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50')
if ced5 > 0:
    print(f'Total de {ced5} cédulas de R$5')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10')
if ced100 > 0:
    print(f'Total de {ced100} cédulas de R$100')
print('='*30)
print('Volte sempre ao BANCO DO SAULLO! Tenha um bom dia!')