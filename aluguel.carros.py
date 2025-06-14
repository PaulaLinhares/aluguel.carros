dias=float(input("Quantos dias você alugou o carro?"))
km=float(input("Quantos km rodados:"))
carro=(dias*60)+(km*0.15)
print("Você alugou o carro por {:.0f} dias, então \n "
      "o valor a pagar é de R${:.2f}. Pois a diária é R$60 e \n"
      "R$0.15 por km rodado!".format(dias,carro,))