from queue_lists.stack_ll import StackLL
import networkx as nx
import queue as q


def colour5(G):
    def check(w):   #gdy zmienia się stopień - zmienia kolejkę
        if DEG[w] == 5:
            Q5.put(w)
        elif DEG[w] == 4:       #spr czy w dobrej kolejności się dzieje
            v = Q5.get()    #przenies w z Q5 do Q4 (v=w)
            Q4.put(v)

    def delete(v, n):  #delete(Q4.get(), n)
        pointer = L[v]
        for w in L[v]:  #dla każdego sąsiada v: usuń v z N(w), zmniejsz stopień w
            Lw = L[w]
            if v in Lw:
                Lw.remove(v) #v not in L[w]
                DEG[w] -= 1
            print("delete")
            check(w)
        S.push((v, pointer))
        ### delete from Qi the node pointed to by DP[v]
        n -= 1

    def identify(u, v, n):
        for w in L[v]: #type(w) = int
            for i in range(len(MARK[w])):
                MARK[w][i] = True
        for w in L[u]:
            if u in L[w]:
                L[w].remove(u)    #dla każdego sąsiada u - usuń u z jego sąsiadów
            if not MARK[w]:  # w sasiaduje z u i nie sasiaduje z v
                L[v].append(w)  #połącz je
                L[w].append(v)
                DEG[v] += 1
                if DEG[v] == 6:
                    Q5.get()  #usun v z Q5
                elif DEG[v] == 5:
                    Q5.get()  #przenies v z Q4 do Q5
                    Q4.put(w)
            DEG[w] -= 1  #jeśli to sąsiad u i v
            check(w)
        for w in L[v]:
            MARK[w] = False
        print(set(Q5))
        if u in Q5:   #delete u from Qi
            Q5.get()
        elif u in Q4:
            Q4.get()
        S.push((u,v))
        n -= 1
    print("identify")

    def reduce(n):
        print("reduce1")
        while n > 5:
            if not Q4.empty():
                print("reduce3")
                delete(Q4.get(), n)
            v = Q5.get()
            print("reduce2")
            for x in G.neighbors(v):
                for y in G.neighbors(v):
                    if not (x == y or y in G.neighbors(x)) and DEG[x] < k and DEG[y] < k: #jeśli 2 niepołączone sąsiady v mają stopnie < k=6
                        delete(v, n)
                        identify(x, y, n)
                    Q5.put(v)  #else: return v to the end of Q5
            print("reduce4")

    def colour():
        print("colour")
        result = []
        l = ["red", "blue", "yellow", "green", "orange"]
        for _ in range(Q4.qsize()):
            v = Q4.get()
            result[v] = l.pop()
            #v["colour"] = l.pop()
            #result.append(v)
        while not S.is_empty():
            (x,y) = S.pop()
            l = ["red", "blue", "yellow", "green", "orange"]
            if type(y) == list:  #jeśli y to lista (wskaźnik do L) => pokoloruj x innym kolorem niż węzły z y
                for u in y:
                    l.remove(result[u])
                result[x] = l.pop()
            x["colour"] = y["colour"] #jeśli y to węzeł, z którym x był zidentyfikowany => pokoloruj na ten sam kolor co węzeł y
        return result

    #-------------colour5----------------------
    k = 6  #istnieje węzeł stopnia < 6
    n = G.number_of_nodes()
    S = StackLL()
    MARK, DEG, L = [], [], []
    Q4, Q5 = q.Queue(), q.Queue()
    #Q4, Q5 = QueueLL(), QueueLL() #kolejki zawierające węzły stopnia <=4 i =5
    for node in G:
        v = node
        L.append(list(G.neighbors(v)))    #L - lista połączeń (lista list)
        deg = G.degree(v)
        DEG.append(deg)    #DEG - lista stopni wierzchołków
        if deg <= 4:
            Q4.put(v)
        elif deg == 5:
            Q5.put(v)
        neighbours = []
        for _ in list(G.neighbors(v)):
            neighbours.append(False)
        MARK.append(neighbours)  #[[False, False, ..], [False, False, ..], .. ] - lista list
    reduce(n)
    colour()


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
    #print(colour5(g))
    I = nx.icosahedral_graph()
    print(colour5(I))