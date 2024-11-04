print("Teste")
def obter_informacoes_usuario():
    nome = input("Qual é o seu nome ")
    idade = int(input("Digite sua idade: "))
    return nome, idade
nome, idade = obter_informacoes_usuario()
print(f"Olá, {nome}! Você tem {idade} anos.")

def realizar_operacoes_matematicas(numero1, numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2
    return soma, subtracao, multiplicacao, divisao

nome, idade = obter_informacoes_usuario()
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma, subtracao, multiplicacao, divisao = realizar_operacoes_matematicas(numero1, numero2)

for i in range(5):
    print("Olá!")

import time  

while True:
    print("O Palmeiras não tem mundial")
    time.sleep(1)  

    if input() == 'K':
        break  
