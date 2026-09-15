def calcula_tabuada(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
        
def somar_valores(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
        print(f'Soma até {i}: {soma}')
    return soma        