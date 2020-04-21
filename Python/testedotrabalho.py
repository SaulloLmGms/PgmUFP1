print ('=' * 30)
print ( '{:^30}' .format ('BANCO DO SAULLO'))
print ('=' * 30)

print('Bem vindo ao Banco do Saullo')

print('Digite 1 para Carregar o caixa eletrônico; Digite 2 para Sacar Dinheiro; Digite 3 para Sair')

saldo = 0
count = 'yes'
while count == 'yes':
    opção = int(input('Digite a operação que deseja realizar: '))
    if opção == 1:
        saldo += int(input('Quanto você quer depositar? Eu quero depositar R$: '))
    elif opção == 2:
        valor = int(input('Qual valor você quer sacar? R$ '))
        total = valor
        ced = 100
        totalced = 0

        if (valor % 5 == 0) and (saldo >= valor):
            saldo -= valor
            while True:
                if total >= ced:
                    total -= ced
                    totalced += 1
                else:
                    if totalced > 0:
                        print(f'Total de {totalced} cédulas de R$ {ced}')
                    if ced == 100:
                        ced = 50
                    elif ced == 50:
                        ced = 20
                    elif ced == 20:
                        ced = 10
                    elif ced == 10:
                        ced = 5
                    totalced = 0
                    if total == 0:
                        print("Concluido!")
                        break
        else:
            print("Você não pode sacar esta quantia... Tente novamente!")
    elif opção == 3:
        count = 'no'

print("Muito obrigado por utilizar o Banco do Saullo! Volte sempre!")