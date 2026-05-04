#atividade 1

tri1 = 55
tri2 = 61
tri3 = 86
resultado = tri1 + tri2 + tri3
i = "matheus"

if  resultado >= 180:
    print("A pontuacao do aluno "+i+" foi de "+str(resultado)+" "
    "entao foi aprovado")
else:
    print("A pontuacao do aluno "+i+" foi de "+str(resultado)+" "
    "entao foi reprovado")


# atividade 2

letras=input("digite uma dessas letras(A,T,C,G)").upper()
if letras== 'A':
    print('T')

elif letras == 'T':
    print('A')

elif letras == 'C':
    print('G')

elif letras == 'G':
    print('C')

else:
    print("letra invalida!")

#atividade 3

num = int(input("escolha um numero"))

num2 = int(input("escolha outro numero"))

print("1)soma de 2 numero")

print("2)diferença entre 2 numeros")

print("3) produto entre 2 numero")

print("4)divisao entre 2 numero")

prince = input("digite o numero da opçao escolhida")

if  prince == "1":
    result = num + num2
    print("seu resultado",result)

elif prince == "2":
    result = num > num2
    print("seu resultado",result)

elif prince == "3":
    result = num * num2
    print("seu resultado",result)

elif prince == "4":
    if num2 != 0:
        result = num / num2
        print("seu Resultado:", result)
    else:
        print("nao e possivel dividir por zero")

else:
    print("Opcao invalida")



#atividade 4



sexo = input("Digite o seu sexo (M/F): ")
idade = int(input("Digite a sua idade: "))

sexo = sexo.lower()

if idade < 10 or idade > 65:
    valor = 0.50

elif idade <= 17:

    valor = 4.28

elif sexo == "f":

    valor = 5.50

else:

    valor = 8.25

print("Valor a pagar: R$", valor)