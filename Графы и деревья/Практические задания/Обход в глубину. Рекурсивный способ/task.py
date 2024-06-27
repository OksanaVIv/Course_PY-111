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


    # """Вариант без рекурсии. Копия с  Обхода в ширину, отличие только в том,
    # что current_node = d.popleft() заменили на current_node = d.pop()"""
    # visited = {node: False for node in g.nodes}
    # d = deque()
    # path = []
    #
    # d.append(start_node)
    # visited[start_node] = True
    #
    # while d:
    #     current_node = d.pop()
    #     path.append(current_node)
    #
    #     for neighbor in g.neighbors(current_node):
    #         if not visited[neighbor]:
    #             d.append(neighbor)
    #             visited[neighbor] = True
    # return path
    #

    """Вариант с рекурсией"""
    visited = {node: False for node in g.nodes}
    path = []

    def rec_dfs(current_node):
        visited[current_node] = True
        path.append(current_node)

        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                rec_dfs(neighbor)

    rec_dfs(start_node)

    return path

if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
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