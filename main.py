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
    y = [2,1,1,8]
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
        if not verificalista(tupla) == True: vec.append(tupla)

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
        
        if temp in vec2: next
        else: vec2.append(temp)
    # vec2 = list(vec2)
    for i in x:
        tupla = ()
        vec2.append( ((int(540 / i)), i) )
    print(vec2)
    return vec2

def combinacoes(pedidos):

    matriz_eq = [ [] for i in range(len(pedidos)) ] # cria uma matriz de tamanho N pedidos x M equacoes
    print(matriz_eq)
    x = 0
    y = 0
    print("hum: \n ",pedidos, "\n *** \n")
    for c in pedidos:
        j = 1
        y = 0
        for c1 in pedidos: #eu to fazendo tudo do 0, tem como comecar da posicao atual de pedidos?
            temp = pedidos[c][1] 
            while ( (temp+pedidos[c1][1]) < 540): #tempo de um dia de trabalho-maquina 
                temp+=pedidos[c1][1]
                j+=1 # quantidade de vezes que aquele tempo X pode aparecer combinando com os outros pedidos
            # print("valor x: ", x, " valor y: ", y, "\n")
            print("valor c: ", c, " valor c1: ", c1, "\n")
            if c != c1:
                print("entrou aqui != \n")
                matriz_eq[x].append(j) # x representa qual eh a linha da equacao que simultaneamente eh a eq de restricao do tempo
            elif c == c1:
                print("entrou aqui == c1 ", c1, "**** x: ", x, "\n")
                matriz_eq[x].append(j)
            j = 0
            y+=1
        x+=1

    print("yey \n")
    print(matriz_eq)

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
    teste = leitura()
    print("valor de teste: \n", teste)
    tempos = integridade(teste) #retorna um dicionario com os tempo de forma de chave e seu conteudo uma tupla com quantidade de pedidos para aquele tempo. (n,t)
    
    testeru(tempos)

  


    # combinacoes(tempos)

if __name__ == "__main__":
    main()