#Projeto da Disciplina Teoria e Aplicação de Grafos - UnB
# 15/7/2022
# 202006448
# Rafael Hamú

#Dados retirados desses sites :
# - https://en.wikipedia.org/wiki/Bron–Kerbosch_algorithm
# - https://www.youtube.com/watch?v=j_uQChgo72I
# - Monitoria antiga de TAG.

import random
from collections import defaultdict


class Grafo: #cria o grafo
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        self.arestas = defaultdict(set)
        
    def adiciona_arestas(self,u,v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)
        
        

    def mostra_lista(self): #cria a lista de adjacencia
        for i in range(self.vertices):
            lista_test = []
            
            for j in self.grafo[i]:
                lista_test.append(j)  

            lista_adjacencia.append(lista_test)
        return lista_adjacencia
        #print(f'{lista_adjacencia}')


def BK_sem_pivo(P, R=None, X=None): #Inicia o Algoritmo sem Pivoteamento
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R  
    while P:
        v = P.pop()
        yield from BK_sem_pivo(
            P=P.intersection(d[v]), R=R.union([v]), X=X.intersection(d[v]))
        X.add(v)

def BK_com_pivo(P, R=None, X=None): #Inicia o Algoritmo com Pivoteamento
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    try:
        u = random.choice(list(P.union(X)))  # escolhe um pivo aleatorio
        Z = P.difference(d[u])
    except IndexError:  # caso u nao esteja na lista.
        Z = P
    for v in Z:
        yield from BK_com_pivo(
            P=P.intersection(d[v]), R=R.union([v]), X=X.intersection(d[v]))
        P.remove(v)
        X.add(v)
d = {}
g = Grafo(62)
graph_updated = []
lista_adjacencia = []
lista_test = []
with open("soc-dolphins.mtx",'r') as arquivo: #le o arquivo de grafos
    grafos = []
    lines = arquivo.readlines()
  
for i in range(len(lines)) :
    grafos.append(lines[i].strip('\n'))    #strip '\n'
grafos = [grafos.replace(' ',',')for grafos in grafos]

for i in grafos: #transformar a string do arquivo em int
    splitado = i.split(',')
    value, key = splitado
    if key in d: #cria a lista de adjacencias no dicionario
        d[key].append(value)
    else:
        d[key] = [value]

    graph_updated.append(splitado)
P = d.keys()
graph_updated = [list(map(int, x)) for x in graph_updated]
for i in graph_updated:
    g.adiciona_arestas(i[0],i[1])
print('ALGORITMO SEM PIVOTEAMENTO :')
print()
print(f'Foram {len(list(BK_sem_pivo(P)))} cliques')
print(f'Cliques Maximais Encontrados: {list(BK_sem_pivo(P))}')
print('---------------------------------------------------')
print('---------------------------------------------------')
print('ALGORITMO COM PIVOTEAMENTO :')
print(f'Foram {len(list(BK_com_pivo(P)))} cliques')
print(f'Cliques Maximais Encontrados: {list(BK_com_pivo(P))}')
