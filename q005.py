print("Assim que você digitar o número, te mostro a tabuada dele. Prático?!")

n = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))

print("Fim do programa!")