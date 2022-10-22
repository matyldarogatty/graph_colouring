import networkx as nx
import matplotlib.pyplot as plt
import random


def coloring_v1(graph):
    colors = ["red", "green", "blue", "orange", "pink"]
    color_map = []
    for _ in graph:
        color_map.append('blue')
    for node in graph:
        for nbr in graph[node]:
            if color_map[node] == color_map[nbr]:
                colors.remove(color_map[node])
                color_map[nbr] = random.choice(colors)
                colors.append(color_map[node])
    for node in graph:
        for nbr in graph[node]:
            if color_map[node] == color_map[nbr]:
                colors.remove(color_map[node])
                color_map[nbr] = random.choice(colors)
                colors.append(color_map[node])
    nx.draw(graph, node_color=color_map, with_labels=True)
    plt.show()


if __name__ == "__main__":
    G = nx.complete_graph(5)
    H = nx.gnp_random_graph(10, 0.5)
    R = nx.erdos_renyi_graph(20, 0.1)
    coloring_v1(G)
    coloring_v1(H)
    coloring_v1(R)


