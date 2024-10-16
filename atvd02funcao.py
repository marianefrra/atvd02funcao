# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar

num = int(input("Digite seu numero:"))

def verificar_paridade(num):
    if num %2 == 0:
        return "O numero é par"
    else:
        return "O numero é impar"
    
mari=verificar_paridade(num)
print(mari)