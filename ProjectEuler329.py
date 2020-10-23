
coaxar = {}

#Teste para saber se é numero primo
def primo(i): 
    if i <= 1: 
        return False
    for n in range(2,i): 
        if i % n == 0: 
            return False
    return True

#Define a probabilidade do coaxar do sapo para primos e não primos
for i in range(1, 501):
    if primo(i) == 1:
        coaxar[(i, 'P')] = 2/3
        coaxar[(i, 'N')] = 1/3
    else:
        coaxar[(i, 'P')] = 1/3
        coaxar[(i, 'N')] = 2/3

#Calcula a probabilidade para cada salto
def calc_prob(i, string):
    if (i, string) in coaxar:
        return coaxar[(i, string)]
    
    if (i == 1):
        prob = coaxar[(i, string[0])] * calc_prob(i + 1, string[1:])
    elif (i == 500):
        prob = coaxar[(i, string[0])] * calc_prob(i - 1, string[1:])
    else:
        prob = coaxar[(i, string[0])] * (calc_prob(i + 1, string[1:]) * 1/2 + calc_prob(i - 1, string[1:]) * 1/2)
    
    coaxar[(i, string)] = prob
    return prob

if __name__ == '__main__':
	resultado = 0
	for i in range(1, 501):
		resultado += calc_prob(i, 'PPPPNNPPPNPPNPN')   #Chama a probabilidade de acordo com quantas coaxadas que o sapo realizara 
	print("O resultado é:", resultado/500)                 #Resultado baseado na probabilidade pelo número de quadrados
