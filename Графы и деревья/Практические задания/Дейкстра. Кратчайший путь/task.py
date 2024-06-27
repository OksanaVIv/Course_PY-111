from typing import Hashable, Mapping, Union
import networkx as nx
import heapq


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Функция с помощью алгоритма Дейкстры из модуля NetworkX находит кратчайшие пути до всех достижимых вершин графа.
    Если вершина не достижима, то стоимость пути до неё должна быть равно float("inf")

    :param g: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :param starting_node: Стартовый узел, откуда нужно начать обход
    :return: словарь как {'node1': 0, 'node2': 10, '3': 33, ...} со стоимостью путей, где node1, node2 - это узлы из графа g
    """
     # TODO вернуть стоимость путей до всех вершин посчитанных алгоритмом Дейкстры
    distances = {node: float('inf') for node in g.nodes}
    distances[starting_node] = 0
    predecessor = {node: None for node in g.nodes}

    queue = [(0,starting_node)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbour, weigh in g[current_node].items():
            distance = current_distance + weigh['weigh']
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                predecessor[neighbour] = current_node
                heapq.heappush[queue, (distance, neighbour)]

    return distances, predecessor

if __name__ == '__main__':

    graph = nx.DiGraph
    graph.add_weighted_edges_from([

    ])

    print(dijkstra_algo(graph, 1))  # {1: 0, 2: 7, 3: 9, 6: 11, 4: 20, 5: 26}
