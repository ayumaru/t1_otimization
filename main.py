import sys
import argparse
import fileinput
from itertools import groupby,combinations, combinations_with_replacement

"""
Para cada conjunto de chave do pedido, verificar uma combinação da chave X com todas as outras (incluindo ela mesma), para saber quantos valores dela podem aparecer
Vai estar seguindo a ordem de entrada, nao necessariamente vai ser do menor para o maior
E se eu achar o maximo de vezes que a variavel X pode ser utilizada sozinha, ai ir subtraindo esse maximo e adicionando outras Y ate extrapolar
---

E se eu pegar o valor de cada tempo e ir armazenando por vez, exemplo
guardo 200
faco 200 + 200 = 400 (guardo 200 novamente)
faco soma dos anteriores + 200 ( deu maior que deveria? Entao desfaz a ultima soma)
mantem a soma temporaria e vai para o proximo elemento de tempo, (tenta somar ele, caso nao de vai pro passo 3) , faz todas as combinacoes para aquela soma ali, nao deu vai para proxima

problema da mochila com memoria

"""




def verificalista(lst):
    return len(set(lst)) == 1

def testeru(x):
    # x = [100, 200, 300]
    x = [200,330,420,500]
    y = [10,5,10,8]
    t = []
    j = 1
    flag = 1
    while (flag):
        flag = 0
        # print(list(combinations_with_replacement(x,j)))
        for k in list(combinations_with_replacement(x,j)):
            if sum(list(k)) <= 540:
                t.append(k)
                flag = 1
            else:
                break
        j+=1

    # print(t)z
    vec = []
    for tupla in t:
        flag = 0
        for i in tupla:
            if (i != 100):
                flag = 1
                break
        if (flag == 1):
            next
        if not verificalista(tupla) == True:
            vec.append(tupla)

    vec1 = []
    for x1 in x:
        for tupla in vec:
            if (sum(tupla) + 100 < 540): next
            else: vec1.append(tupla)


    vec2 = []
    for h in vec1:
        temp = []
        for tuplas in x:
            if h.count(tuplas) != 0:
                temp.append(h.count(tuplas))
                temp.append(tuplas)
        
        if temp in vec2:
            next
        else:
            vec2.append(temp)
    

    for i in x:
        if i+min(x) > 540 or i == min(x): 
            hm = [(int(540 / i)), i]
            vec2.append(hm)

    

    # x = [200,330,420,500]
    y = { 200: (10,200), 330: (5,330) , 420: (10, 500) , 500: (8,500) }
    # y = {100: (4,100), 200: (5,200), 300: (6,300) }
    matriz = []
    temp = [ 0 for i,_ in enumerate(vec2)]
    print("before .. ",vec2)
    # ver como contornar o fato que ele ta pegando de um grupo que ja foi pego
    for i in y: #aqui tenho a chave
        l = 0
        for j in vec2: # aqui vou pegar cada lista 
            if i in j: #esta dentro do vetor de pedidos 
                ind = j.index(i)
                temp[l] = (j[ind-1])
            l+=1
        matriz.append(temp)       
        temp = [ 0 for i,_ in enumerate(vec2) ]
        # break
    print("matriz vem a baixo")
    print(matriz) #tenho a matriz de pedidos
    
    #como a matriz foi criada usando a ordem das coisas presentes no dicionario
    vars =[]
    # for i,_ in enumerate(matriz): #problema eh isso ai
     #     vars.append("x" + str(i))
    
    g = []
    for i in matriz:
        g.append(len(i))
    for i in range(0,max(g)):
        vars.append("x" + str(i))
    print(vars)

    f_desejado = 'min: ' + (' + '.join( str(v) for v in vars )) + ';\n'
    print(f_desejado)
    print(vars)

    print("aqui")
    # for i in y: 
    for i,j in zip(y,matriz):
        rest = []
        v = 0
        for k in j: #elementos da linha da matris
            if k > 0:
                # print(str(k)+vars[v])
                rest.append( f'{k}{vars[v]}') 
            v+=1
        v = 0 
        print(*rest, sep = " + ", end='')
        print(' >= ', y[i][0], ';')



def tratamento(dado):
    numeros = []
    for valores in dado:
        temp = valores.split()
        for i in temp:
            if i.isdigit():
                numeros.append(int(i))
    return numeros

"""
verificar se num de maquinas e inteiro
verificar se num de pedidos de tempo sao inteiros
sei que indice 0 e indice 1 sao sempre maquina e quantidade de tempos
indices impares comecando do 3, sao a representacao do tempo desejado para o pedido
"""
def integridade( entrada ): #verificacao dos parametros passados para resolucao
    
    temp = tratamento(entrada)
    if (temp[0] <= 0): #nao ta usando pcs
        exit("A quantidade de computadores passada nao esta dentro dos valores permitidos. Obrigatorio: computadores > 0")
    if (temp[1] < 1): #pedidos de tempo negativo ou nao ta pedindo tempo
        exit("A quantidade de pedidos de para utilizar o sistema nao esta dentro do permitido. Obrigatorio: pedidos > 0")

    pedidos = temp[1]

    if ( ( (len(temp)/2)-1) != pedidos ):
        print("A quantidade de tempos fornecidas nao batem com a especificacao passada pelo valor de quantidade de pedidos.")
        print("Quantidade de Tempos fonecidos: ", len(temp)/2-1, "\n Quantidade de pedidos fornecido: ", pedidos, "\n")
        exit("Dados incorretos.")

    t_exec = {}
    for i in range( 3, len(temp), 2):
        if temp[i] > 540:
            exit("Um dos tempos de pedido informado excede a carga diaria de trabalho: 540 minutos ou 9 horas.") 
        t_exec[temp[i]] = (temp[i-1], temp[i]) # (Ni, Ti)

    if (len(t_exec) != pedidos):
        exit("Inconsistencia de dados. Existem pedidos duplicados com a mesma quantidade de tempo de execucao.") 

    return t_exec


def leitura(): #depois dar uma olhada para dar merge em tratamento + leitura
    entrada = []
    for linha in fileinput.input():
        entrada.append( linha.rstrip() )
    return entrada


def main():
    teste = leitura() # vai ter que arrumar leitura
    # print("valor de teste: \n", teste)
    tempos = integridade(teste) #retorna um dicionario com os tempo de forma de chave e seu conteudo uma tupla com quantidade de pedidos para aquele tempo. (n,t)
    
    testeru(tempos)

  


    # combinacoes(tempos)

if __name__ == "__main__":
    main()