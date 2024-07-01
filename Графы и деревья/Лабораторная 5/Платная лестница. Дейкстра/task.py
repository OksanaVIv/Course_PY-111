from typing import Union
from typing import List

import networkx as nx

def graph_create(stairway:List) -> List:
    graph_base = []
    for i in range(len(stairway)):
        graph_base.append((i, i+1, stairway[i]))
    for i in range(len(stairway)-1):
        graph_base.append((i, i+2, stairway[i+1]))
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(graph_base)
    return graph

def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
     # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    end_step = list(stairway_graph.nodes())[-1]
    return nx.shortest_path_length(graph, source=0, target=end_step, weight="weight")



if __name__ == '__main__':
    # stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway = (4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2)
    stairway_graph = graph_create(stairway)  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
