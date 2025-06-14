# Projeto Via PyCharm
dias=float(input("Quantos dias você alugou o carro?"))
km=float(input("Quantos km rodados:"))
carro=(dias*60)+(km*0.15)
print("Você alugou o carro por {:.0f} dias, então \n "
      "o valor a pagar é de R${:.2f}. Pois a diária é R$60 e \n"
      "R$0.15 por km rodado!".format(dias,carro,))

O Projeto mostra quantos reais o locatário terá que pagar pelo aluguel
do carro de acordo com a quantidade de dias que ele usou.
Criado com dedicação por Paula Linhares 🛠
