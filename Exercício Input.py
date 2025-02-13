nome = input ("Insira o seu nome: ")
sobrenome = input ("Insira o seu sobrenome: ")
endereco = input ("Digite o seu endereço: ")
cargo = input ("Digite o seu cargo: ")
salario = float (input ("Digite o seu salário atual: "))

porcen =(salario * 0.08)

aumento = salario + porcen


print ("Olá ",nome, sobrenome)
print ("O seu cargo é :", cargo)
print ("Você receberá um aumento de 8% no valor de: R$", porcen)
print ("Seu salário foi para R$", aumento)
