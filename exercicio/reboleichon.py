x = float(input("Escreva um numero:"))
resto = x % 2

if resto != 0 :
        print("Estranho")
elif resto == 0 and x >= 2 and x <= 5 :
        print("Não é estranho")
elif resto == 0 and x >= 6 and x <= 20:
        print("Estranho")
elif resto == 0 and x > 20:
        print("Não é estranho")