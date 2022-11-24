from queue_lists.queue_ll import QueueLL
from structures.graph import Graph
from queue_lists.stack_ll import StackLL
import networkx as nx


def colour5(G):
    def adjacency_list(v):
        lst = []
        for u in v.get_connections():
            lst.append(u.id)
        return lst

    def check(w):   #gdy zmienia się stopień - zmienia kolejkę
        if DEG[w] == 5:
            Q5.enqueue(w)
        elif DEG[w] == 4:       #spr czy w dobrej kolejności się dzieje
            Q5.dequeue()    #przenies w z Q5 do Q4
            Q4.enqueue(w)

    def delete(v, n):
        for w in L[v]:  #dla każdego sąsiada v: usuń v z N(w), zmniejsz stopień w
            Lw = L[w]
            Lw.remove(v)
            DEG[w] -= 1
            check(w)
        S.push((v, L[v].index(v)))
        ### delete from Qi the node pointed to by DP[v]
        n -= 1

    def identify(u, v, n):
        for w in L[v.id]: #type(w) = int (vert.id)
            for i in range(len(MARK[w])):
                MARK[w][i] = True
        for w in L[u.id]:
            L[w].remove(u.id)    #dla każdego sąsiada u - usuń u z jego sąsiadów
            if not MARK[w]:  # w sasiaduje z u i nie sasiaduje z v
                L[v.id].append(w)  #połącz je
                L[w].append(v.id)
                DEG[v] += 1
                if DEG[v] == 6:
                    Q5.dequeue()  #usun v z Q5
                elif DEG[v] == 5:
                    Q5.dequeue()  #przenies v z Q4 do Q5
                    Q4.enqueue(w)
            DEG[w] -= 1
            check(w)
        for w in L[v]:
            MARK[w] = False
        #delete u from Qi
        #push (u,v) on to S
        n -= 1

    def reduce(n):
        while n > 5:
            if not Q4.is_empty():
                delete(Q4.dequeue(), n)  #delete top entry from Q4
            #jeśli Q4 jest puste, bierzemy z Q5
            v = Q5.dequeue()
            for x in v.get_connections():
                for y in v.get_connections():
                    if not (x == y or y in x.get_connections()) and DEG[x] < k and DEG[y] < k:#jeśli 2 niepołączone sąsiady v mają stopnie < k=6
                        delete(v,n)
                        identify(x, y, n)
                    Q5.enqueue(v)  #else: return v to the end of Q5

    def colour():
        result = dict()
        #pokoloruj węzły z Q4
        if not Q4.is_empty():
            result["red"] = Q4.dequeue()
        if not Q4.is_empty():
            result["blue"] = Q4.dequeue()
        if not Q4.is_empty():
            result["yellow"] = Q4.dequeue()
        if not Q4.is_empty():
            result["green"] = Q4.dequeue()
        if not Q4.is_empty():
            result["orange"] = Q4.dequeue()
        while not S.is_empty():
            (x,y) = S.pop()
            #if: jeśli y to wskaźnik do listy L => pokoloruj x innym kolorem niż węzeł L[y]
            #else: jeśli y to węzeł, z którym x był 'identified' => pokoloruj na ten sam kolor co węzeł y

    #-------------colour5----------------------
    k = 6  #istnieje węzeł stopnia < 6
    n = G.num_vertices
    S = StackLL()
    MARK, DEG, DP, L = [], [], [], []
    Q4, Q5 = QueueLL(), QueueLL() #kolejki zawierające węzły stopnia <=4 i =5
    for i in range(G.num_vertices):
        v = G.get_vertex(i)
        L.append(adjacency_list(v))  #L - lista połączeń (lista list)
        deg = v.deg()
        DEG.append(deg)   #DEG - lista stopni wierzchołków
        if deg <= 4:
            Q4.enqueue(v)
            #DP[v] zawiera wskaźnik do elementu v w Qi, jeśli v jest w Qi
        elif deg == 5:
            Q5.enqueue(v)
        neighbours = []
        for _ in v.get_connections():
            neighbours.append(False)
        MARK.append(neighbours)  #[[False, False, ..], [False, False, ..], .. ] - lista list
    print(L)
    print(DEG)
    print(Q5)
    print(Q4)
    print(MARK)
    print(DP)
    reduce(n)
    colour()


if __name__ == "__main__":
    g = Graph()

    for i in range(6):
        g.add_vertex(i)
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
    g.add_edge(5, 3)

    colour5(g)