import networkx as nx
import queue as q
import collections
import matplotlib.pyplot as plt


class Colour5:
    def __init__(self, graph, start_from=None):
        self.G = graph
        self.ident, self.blocked = set(), set()
        self.k = 13
        self.n = graph.number_of_nodes()
        self.S = []
        self.L = [list(graph.neighbors(v)) for v in sorted(graph)]
        self.DEG = [graph.degree(v) for v in sorted(graph)]
        self.MARK = [False] * graph.number_of_nodes()
        self.Q4, self.Q5 = collections.deque(), collections.deque()
        # start z konkretnego węzła
        g = sorted(graph)
        if start_from:
            g.remove(start_from)
            g.insert(0, start_from)
        for v in g:
            if graph.degree(v) <= 4:
                self.Q4.append(v)
            elif graph.degree(v) == 5:
                self.Q5.append(v)

    def check(self, w):    #gdy zmienia się stopień - element zmienia kolejkę
        if self.DEG[w] == 5:
            self.Q5.append(w)
        elif self.DEG[w] == 4:
            self.Q5.remove(w)   #przenies w z Q5 do Q4
            self.Q4.append(w)

    def delete(self, v):  #delete(Q4.get(), n)
        pointer = self.L[v][:]
        for w in self.L[v]:  #dla każdego sąsiada v: usuń v z N(w), zmniejsz stopień w
            self.L[w].remove(v) #v not in L[w]
            self.DEG[w] -= 1
            self.check(w)
        self.S.append((v, pointer))
        self.n -= 1

    def identify(self, u, v):
        self.ident.add((u, v))
        for w in self.L[v]:
            self.MARK[w] = True
        for w in self.L[u]:
            self.L[w].remove(u)    #dla każdego sąsiada u - usuń u z jego sąsiadów
            if not self.MARK[w]:  # w sasiaduje z u i nie sasiaduje z v
                self.L[v].append(w)  #połącz je
                self.L[w].append(v)
                self.DEG[v] += 1
                if self.DEG[v] == 6:
                    self.Q5.remove(v)  #usun v z Q5
                elif self.DEG[v] == 5:
                    self.Q4.remove(v)  #przenies v z Q4 do Q5
                    self.Q5.append(v)
            else:
                self.DEG[w] -= 1  #jeśli to sąsiad u i v
                self.check(w)
        for w in self.L[v]:
            self.MARK[w] = False
        if u in self.Q5:   #delete u from Qi
            self.Q5.remove(u)
        elif u in self.Q4:
            self.Q4.remove(u)
        self.S.append((u, v))
        self.n -= 1

    def reduce(self):
        while self.n > 5:
            if self.Q4:
                self.delete(self.Q4.popleft())
            else:
                v = self.Q5.popleft()
                m = False
                for x in self.L[v]:
                    for y in self.L[v]:
                        if not (x == y or y in self.L[x]) and self.DEG[x] < self.k and self.DEG[y] < self.k: #jeśli 2 niepołączone sąsiady v mają stopnie < k=6
                            m = True
                            self.delete(v)
                            self.identify(x, y)
                            break
                    if m:
                        break
                if not m:
                    self.blocked.add(v)
                    self.Q5.append(v)  #'blocked vertex' wraca na konieć Q5

    def colour(self):
        result = {}
        l = {"red", "blue", "yellow", "green", "orange"}
        for _ in range(len(self.Q4)):
            v = self.Q4.popleft()
            result[v] = l.pop()
        l = {"red", "blue", "yellow", "green", "orange"}
        while self.S:
            x, y = self.S.pop()
            if isinstance(y, list):  #jeśli y to lista (wskaźnik do L) => pokoloruj x innym kolorem niż węzły z y
                result[x] = (l - {result[u] for u in y}).pop()
            else:
                result[x] = result[y]  #jeśli y to węzeł, z którym x był zidentyfikowany => pokoloruj na ten sam kolor co węzeł y
        return result

    def start(self):
        self.reduce()
        print("identifications:", self.ident)
        print("blocked vertixes:", self.blocked)
        return self.colour()

    def draw_colouring(self):
        result = self.start()
        col_map = [result[x] for x in self.G]
        nx.draw_planar(self.G, node_color=col_map, with_labels=True)  # , pos=nx.spring_layout(graph)
        plt.show()


if __name__ == "__main__":
    g = nx.Graph()
    for i in range(6):
        g.add_node(i)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(5, 4)
    g.add_edge(5, 2)
    #col = Colour5(g)
    I = nx.icosahedral_graph()
    print(nx.is_planar(I))
    col = Colour5(I)
    col.draw_colouring()


