
print("\n\nOlá UNINASSAU!\n") 
print ("\n***** proxima questão*****")
num1 = float(input("\nDigite um numero: "))
print ("\nO numero foi: ",num1)
print ("\n***** proxima questão*****")
num2 = float(input("\nDigite o primeiro valor: "))
num3 = float(input("\nDigite o segundo valor:  "))
print ("\nA soma dos numeros foi: ",(num2 + num3))
print ("\n***** proxima questão*****")
num4 = float(input("\nDigite a primeira nota: "))
num5 = float(input("\nDigite a segunda nota:  "))
num6 = float(input("\nDigite a terceira nota: "))
num7 = float(input("\nDigite a quarta nota:   "))
print ("\nA media final foi: ",(((num4+num5)+(num6+num7))/4),"\nA nota do primeiro bimestre foi: ",((num4+num5)/2),"\nA nota do segundo bimestre foi:  ",((num6+num7)/2))
print ("\n***** proxima questão*****")
num8 = float(input("\nDigite quantos metros deseja converter: "))
print ("\n",num8,"Metros são: ",num8*100,"centimetros")
print ("\n***** proxima questão*****")
num9 = float(input("\nDigite o raio do circulo: "))
print ("\n A área do circulo é: ",(3.1415*num9**2),"m²")
print ("\n***** proxima questão*****")
num10 = float(input("\nDigite a altura do quadrado: "))
print ("\nA área do quadrado é: ",(num10**2),"m²","\nE o dobro dela é:     ",(num10**2)*2,"m²")
print ("\n***** proxima questão*****")
num11 = float(input("\nQual o valor da hora?    "))
num12 = float(input("Quantas horas trabalhadas por mês? "))
print ("\nO ganho mensal é: R$",num11*num12)
print ("\n***** proxima questão*****")
num13 = float(input("\nDigite um numero, que digo se é ou nao positivo: "))
if num13 < 0:
 print("\nO numero ",num13," é negativo")
elif num13 > 0:
 print("\nO numero ",num13," é positivo")
else: 
 print("\nO numero ",num13," é neutro")
print ("\n***** proxima questão*****")
while True:
 num14 = input("\nDigite \nF - Feminino\nM - Masculino\n")
 num14 = num14.upper()
 if num14 == "F":
  print("\nVocê escolheu Feminino\n")
  break
 elif num14 == "M":
  print("\nVocê escolheu Masculino\n")
  break
 else:
  print("\nSexo invalido")
print("\n***** ACABOU *****")