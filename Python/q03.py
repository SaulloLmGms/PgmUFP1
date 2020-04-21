print("Vamos saber quantos dias tem esse mês nesse ano.")
month = int(input("Digite um mês: "))
year = int(input("Digite um ano: "))
if month > 0 and month <= 12:
    if month == 4 or month == 6 or month == 9 or month == 11:
        print("Esse mês tem", 30 , "dias" )
    else:
        if month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 != 0:
                print("Esse mês tem", 28 , "dias" )
            else:
                print("Esse mês tem", 29 , "dias" )
        else:
            print("Esse mês tem", 31 , "dias" )
else:
    print("Não existe no nosso calendário")
print("Fim do programa.")