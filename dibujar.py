import networkx as nx
import matplotlib.pyplot as plt


def agregar_arista(G, u, v, w=1):
    G.add_edge(u, v, weight=w)

    G.add_edge(v, u, weight=w)

def crearGrafo(edges=[]):
    G=nx.DiGraph()
    for e in edges:
        agregar_arista(G,e[0],e[1],e[2])
    
    pos = nx.layout.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo con NetworkX")
    plt.show()
    