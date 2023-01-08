import networkx as nx
import five_colouring_algm
import matplotlib.pyplot as plt


def one_icoshedral():
    I = nx.Graph()
    for i in range(12):
        I.add_node(i)
    I.add_edge(0, 1)
    I.add_edge(1, 2)
    I.add_edge(2, 3)
    I.add_edge(3, 4)
    I.add_edge(4, 5)
    I.add_edge(5, 6)
    I.add_edge(0, 5)
    I.add_edge(0, 11)
    I.add_edge(0, 7)
    I.add_edge(0, 8)
    I.add_edge(1, 8)
    I.add_edge(1, 6)
    I.add_edge(1, 5)
    I.add_edge(2, 8)
    I.add_edge(2, 9)
    I.add_edge(2, 6)
    I.add_edge(3, 6)
    I.add_edge(3, 9)
    I.add_edge(3, 10)
    I.add_edge(4, 10)
    I.add_edge(4, 11)
    I.add_edge(4, 6)
    I.add_edge(5, 11)
    I.add_edge(7, 8)
    I.add_edge(7, 9)
    I.add_edge(7, 10)
    I.add_edge(7, 11)
    I.add_edge(9, 10)
    I.add_edge(9, 8)
    I.add_edge(10, 11)
    return I


def three_icoshedral():
    I = nx.Graph()
    for p in {0, 12, 24}:
        I.add_edge(0+p, 1+p)
        I.add_edge(1+p, 2+p)
        I.add_edge(2+p, 3+p)
        I.add_edge(3+p, 4+p)
        I.add_edge(4+p, 5+p)
        I.add_edge(5+p, 6+p)
        I.add_edge(0+p, 5+p)
        I.add_edge(0+p, 11+p)
        I.add_edge(0+p, 7+p)
        I.add_edge(0+p, 8+p)
        I.add_edge(1+p, 8+p)
        I.add_edge(1+p, 6+p)
        I.add_edge(1+p, 5+p)
        I.add_edge(2+p, 8+p)
        I.add_edge(2+p, 9+p)
        I.add_edge(2+p, 6+p)
        I.add_edge(3+p, 6+p)
        I.add_edge(3+p, 9+p)
        I.add_edge(3+p, 10+p)
        I.add_edge(4+p, 10+p)
        I.add_edge(4+p, 11+p)
        I.add_edge(4+p, 6+p)
        I.add_edge(5+p, 11+p)
        I.add_edge(7+p, 8+p)
        I.add_edge(7+p, 9+p)
        I.add_edge(7+p, 10+p)
        I.add_edge(7+p, 11+p)
        I.add_edge(9+p, 10+p)
        I.add_edge(9+p, 8+p)
        I.add_edge(10+p, 11+p)
    I.add_edge(0, 12)
    I.add_edge(1, 24)
    return I


def n_icoshedral(n):
    ''' n between 1 and 12 '''
    I = nx.Graph()
    s = {12*i for i in range(n)}
    for p in s:
        I.add_edge(0+p, 1+p)
        I.add_edge(1+p, 2+p)
        I.add_edge(2+p, 3+p)
        I.add_edge(3+p, 4+p)
        I.add_edge(4+p, 5+p)
        I.add_edge(5+p, 6+p)
        I.add_edge(0+p, 5+p)
        I.add_edge(0+p, 11+p)
        I.add_edge(0+p, 7+p)
        I.add_edge(0+p, 8+p)
        I.add_edge(1+p, 8+p)
        I.add_edge(1+p, 6+p)
        I.add_edge(1+p, 5+p)
        I.add_edge(2+p, 8+p)
        I.add_edge(2+p, 9+p)
        I.add_edge(2+p, 6+p)
        I.add_edge(3+p, 6+p)
        I.add_edge(3+p, 9+p)
        I.add_edge(3+p, 10+p)
        I.add_edge(4+p, 10+p)
        I.add_edge(4+p, 11+p)
        I.add_edge(4+p, 6+p)
        I.add_edge(5+p, 11+p)
        I.add_edge(7+p, 8+p)
        I.add_edge(7+p, 9+p)
        I.add_edge(7+p, 10+p)
        I.add_edge(7+p, 11+p)
        I.add_edge(9+p, 10+p)
        I.add_edge(9+p, 8+p)
        I.add_edge(10+p, 11+p)
    for i in range(1, n):
        I.add_edge(i-1, 12*i)
    return I


#one blocked
#G = n_icoshedral(4)
#G.add_edge(25, 1)
#print(G.number_of_edges())
#five_colouring_algm.Colour5(G, 8).draw_colouring()
G = n_icoshedral(3)
G.add_edge(2, 25)
#print(G.number_of_edges())
five_colouring_algm.Colour5(G, 8).draw_colouring()

#nx.draw_planar(I, with_labels=True)#, pos=nx.spring_layout(graph)
#plt.show()