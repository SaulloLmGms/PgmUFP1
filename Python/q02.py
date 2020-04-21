print("Vamos saber se o ano é bissexto ou não")
year = int(input("Digite o ano: "))
if year % 4==0 and year % 100 != 0 and year % 400!= 0:
    print("O ano é bissexto! ")
else:
    print("O ano não é bissexto! ")
print("Fim!")