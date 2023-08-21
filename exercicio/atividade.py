n=int(input("Quantidade de trabalhadores: "))
cont=1
top=0
l1=[]
l2=[]

while cont<=n:
    vendedor = str(input("Nome do vendedor: "))
    num = int(input("Numero da loja do vendedor: "))
    valorzinho = float(input("Valor vendido: "))
    valorzao=valorzinho+(8/100*valorzinho)
    l1.append(vendedor)
    if valorzao>top:
        top=valorzao
        aux=vendedor
    l2.append(valorzao)
    cont=cont+1

valor=max(l2)+300
t=l2.index(max(l2))
l2[t]=valor

print ("Quem vendeu mais foi: ", aux)
print ("Lista dos vendedores: ")
print (l1)
print ("Lista com os valores totais: ")
print (l2)