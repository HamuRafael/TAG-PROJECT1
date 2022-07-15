class Grafo: #cria o grafo
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    def adiciona_arestas(self,u,v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)

    def mostra_lista(self): #cria a lista de adjacencia
        for i in range(self.vertices):
            lista_test = []
            
            for j in self.grafo[i]:
                lista_test.append(j)  

            lista_adjacencia.append(lista_test)
        print(f'{lista_adjacencia}')

def intersec(lista1, lista2):
    """ Função que recebe duas listas e retorna a intersecção entre elas """
    
    return [item for item in lista1 if item in lista2]
def VizinhosDe(vertice):

    return grafos[len(vertice) - 1]


def bronk(R,P,X):
    if len(P) == 0 and len(X) == 0:
        print(R)
        return
    Paux = P.copy()  # Lista auxiliar
    for vertice in P:
        vizinhos = VizinhosDe(vertice)
        bronk(R+[vertice], intersec(Paux, vizinhos), intersec(X, vizinhos))  # Chamada recursiva da função
        Paux.remove(vertice)
        X.append(vertice)
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
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

    graph_updated.append(splitado)
print(d)
graph_updated = [list(map(int, x)) for x in graph_updated]


for i in graph_updated:
    g.adiciona_arestas(i[0],i[1])

g.mostra_lista()

