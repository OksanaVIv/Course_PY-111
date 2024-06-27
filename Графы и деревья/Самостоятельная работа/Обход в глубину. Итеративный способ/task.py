from typing import Hashable, List
from collections import deque

import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """

    visited = {node: False for node in g.nodes}
    d = deque()
    path = []

    d.append(start_node)
    visited[start_node] = True

    while d:
        current_node = d.pop()
        path.append(current_node)

        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                d.append(neighbor)
                visited[neighbor] = True
    return path

if __name__ == '__main__':
    graph = nx.Graph()  # не направленный не мультиграф
    # graph.add_nodes_from('ABCDEFGHIJ')
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('C', 'F'),
        ('B', 'E'),
        ('B', 'D'),
        ('E', 'G'),
    ])
    # nx.draw_networkx(graph)
    # plt.show()
    print(dfs(graph, 'A'))