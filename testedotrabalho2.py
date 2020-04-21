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
        numero = int(input("Informe o valor que você deseja sacar: "))

        if (numero % 5 == 0):
            cem = numero % 100
            notacem = (numero - cem)//100

            cinquenta = cem % 50
            notacinquenta = cem//50

            vinte = cinquenta % 20
            notavinte = cinquenta//20

            dez = vinte % 10
            notadez = vinte//10

            cinco = dez % 5
            notacinco = dez//5

            if saldo < numero:
              print("Não é possivel sacar esta quantia... Tente novamente!")
            else:
                saldo -= numero
                print('''{} Notas de cem
{} Notas de cinquenta
{} Notas de vinte
{} Notas de dez
{} Notas de cinco
    '''.format(notacem, notacinquenta, notavinte, notadez, notacinco))
        else:
            print("Esse valor não pode ser sacado")
    elif opção == 3:
        count = 'no'

print("Muito obrigado por utilizar nossos serviços! Volte sempre!")
print("Att, Banco do Saullo")