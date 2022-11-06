import matplotlib

import networkx as nx
from numpy.random import randint as rnd
import matplotlib.pyplot as plt
#По столбцам, связываем строки с 1
matplotlib.use('TkAgg')


colors_of_nodes = {}


def coloring(node, color):
    for neighbor in G.neighbors(node):
        if neighbor == node:
            continue
        color_of_neighbor = colors_of_nodes.get(neighbor, None)
        if color_of_neighbor == color:
            return False
    return True


colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'Pink', 'Orange', 'White', 'Gray', 'Purple', 'Brown', 'Navy']


def get_color_for_node(node):
    for color in colors:
        if coloring(node, color):
            return color


print("Введите кол-во вершин в графе:", end=" ")
nodes_ = int(input())

matrix = rnd(2, size=(nodes_, nodes_))

# Вывод по горизонтале
index = ""
for i in range(nodes_):
    index += str(i + 1) + " "
print("--", index)

# Вывод по вертикали
for i in range(nodes_):
    print(i + 1, matrix[i])

edges = []
nodesForColor = []
for i in range(0, nodes_):
    for j in range(0, nodes_):
        if (matrix[i, j] == 0):
            continue
        if (matrix[i, j] == 1):
            edges.append((i + 1, j + 1))
arrayNodes = []
G = nx.Graph()
nodes = [i + 1 for i in range(0, nodes_)]
colorsForNodes = []

G.add_nodes_from(nodes)
G.add_edges_from(edges)

print()
print(G.nodes(), "Вершины графа", end=' ... \n')
print(G.edges(), "Ребра графа в формате ВЕРШИНА с ВЕРШИНОЙ")



for node in G.nodes:
    colors_of_nodes[node] = get_color_for_node(node)
    colorsForNodes.append(get_color_for_node(node))
nx.draw(G, node_color=colorsForNodes, with_labels=True)
plt.show()
plt.clf()

for i in range(nodes_ - 1):
    nx.draw(G, node_color=colorsForNodes, with_labels=True)
    plt.show()
    plt.clf()
