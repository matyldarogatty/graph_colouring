from queue_lists.stack_ll import StackLL
import networkx as nx
import queue as q


class Colour5:
    def __init__(self, graph):
        self.G = graph
        self.k = 6  # istnieje węzeł stopnia < 6
        self.n = graph.number_of_nodes()
        self.S = StackLL()
        self.MARK, self.DEG, self.L = [], [], []
        self.Q4, self.Q5 = [], []
        for node in sorted(graph):
            v = node
            print(v)
            self.L.append(list(graph.neighbors(v)))  # L - lista połączeń (lista list)
            deg = graph.degree(v)
            self.DEG.append(deg)  # DEG - lista stopni wierzchołków
            if deg <= 4:
                self.Q4.append(v)
            elif deg == 5:
                self.Q5.append(v)
            self.MARK.append(False)
        print(self.L)
        print(self.DEG)

    def check(self, w):    #gdy zmienia się stopień - element zmienia kolejkę
        if self.DEG[w] == 5:
            self.Q5.append(w)
        elif self.DEG[w] == 4:
            self.Q5.remove(w)   #przenies w z Q5 do Q4 (v=w)
            self.Q4.append(w)

    def delete(self, v):  #delete(Q4.get(), n)
        pointer = self.L[v][:]
        for w in self.L[v]:  #dla każdego sąsiada v: usuń v z N(w), zmniejsz stopień w
            Lw = self.L[w]
            print("delete", w, v, Lw, self.n, self.S)
            Lw.remove(v) #v not in L[w]
            self.DEG[w] -= 1

            self.check(w)
        self.S.push((v, pointer))
        self.n -= 1

    def identify(self, u, v):
        for w in self.L[v]: #type(w) = int
            self.MARK[w] = True
        for w in self.L[u]:
            print("Delete", w, u, self.n, self.S)
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
        self.S.push((u,v))
        self.n -= 1
        print("identify")

    def reduce(self):
        print("reduce1")
        while self.n > 5:
            if self.Q4:
                print("reduce3")
                self.delete(self.Q4.pop(0))
                continue
            else:
                v = self.Q5.pop(0)
                print("reduce2")
                m = False
                for x in self.G.neighbors(v):
                    for y in self.G.neighbors(v):
                        if not (x == y or y in self.G.neighbors(x)) and self.DEG[x] < self.k and self.DEG[y] < self.k: #jeśli 2 niepołączone sąsiady v mają stopnie < k=6
                            m = True
                            self.delete(v)
                            self.identify(x, y)
                            break
                    if m:
                        break
                if not m:
                    self.Q5.append(v)  #'blocked vertex' wraca na konieć Q5
                print("reduce4")

    def colour(self):
        print("colour")
        result = {}
        l = ["red", "blue", "yellow", "green", "orange"]
        for _ in range(len(self.Q4)):
            v = self.Q4.pop(0)
            result[v] = l.pop()
            #v["colour"] = l.pop()
            #result.append(v)
        while not self.S.is_empty():
            (x,y) = self.S.pop()
            l = {"red", "blue", "yellow", "green", "orange"}
            if isinstance(y,list):  #jeśli y to lista (wskaźnik do L) => pokoloruj x innym kolorem niż węzły z y
                result[x] = (l - {result[u] for u in y}).pop()
            else:
                result[x] = result[y]
            #x["colour"] = y["colour"] #jeśli y to węzeł, z którym x był zidentyfikowany => pokoloruj na ten sam kolor co węzeł y
        return result

    def start(self):
        self.reduce()
        return self.colour()


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
    col = Colour5(I)
    result = col.start()
    print(result)
    import matplotlib.pyplot as plt
    col_map = [result[x] for x in I]
    print(col_map)
    nx.draw_planar(I, node_color=col_map, with_labels=True)  # , pos=nx.spring_layout(graph)
    plt.show()
