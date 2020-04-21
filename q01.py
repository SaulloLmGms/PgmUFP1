print("Vamos calcular seu IMC")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso//altura**2
if imc < 18.5:
    print("Você está abaixo do peso: ")
if imc > 25:
    print("Você está acima do peso: ")
if imc <= 25 and imc >= 18.5:
    print("Você está com o peso normal.")
print("Fim do programa.")