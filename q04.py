print("Vamos colocar seus números em ordem")
numero1 = float(input("Digite seu primeiro número: "))
numero2 = float(input("Digite seu segundo número: "))
numero3 = float(input("Digite seu terceiro número: ")) 
if numero1 > numero2 > numero3:
    print(numero1 , numero2 , numero3)
if numero1 > numero3 > numero2:
    print(numero1 , numero3 , numero2)
if numero2 > numero1 > numero3:
    print(numero2 , numero1 , numero3)
if numero2 > numero3 > numero1:
    print(numero2 , numero3 , numero1)
if numero3 > numero1 > numero2:
    print(numero3 , numero1 , numero2)
if numero3 > numero2 > numero1:
    print(numero3 , numero2 , numero1)
if numero1 == numero2 == numero3:
    print(numero1 , numero2 , numero3)
print("Fim!")