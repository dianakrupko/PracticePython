import sys


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    shortest_path = {}

    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node


        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node


        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print("Марштрут знайдено {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


nodes_1 = ["A", "B", "C", "D", "E", "F", "G"]

nodes_2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

init_graph_1 = {}

for node in nodes_1:
    init_graph_1[node] = {}

init_graph_1["A"]["B"] = 5
init_graph_1["A"]["D"] = 8
init_graph_1["B"]["F"] = 1
init_graph_1["B"]["C"] = 3
init_graph_1["C"]["G"] = 5
init_graph_1["A"]["G"] = 6
init_graph_1["E"]["F"] = 2

init_graph_2 = {}
for node in nodes_2:
    init_graph_2[node] = {}

init_graph_2["A"]["E"] = 5
init_graph_2["B"]["I"] = 4
init_graph_2["C"]["F"] = 1
init_graph_2["D"]["K"] = 3
init_graph_2["E"]["N"] = 5
init_graph_2["F"]["O"] = 4
init_graph_2["G"]["H"] = 5
init_graph_2["G"]["L"] = 2
init_graph_2["I"]["N"] = 2
init_graph_2["I"]["M"] = 5
init_graph_2["J"]["L"] = 4
init_graph_2["J"]["K"] = 1
init_graph_2["J"]["O"] = 3


graph_1 = Graph(nodes_1, init_graph_1)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph_1, start_node="A")
print_result(previous_nodes, shortest_path, start_node="A", target_node="F")

print("=====================================================================")
graph_2 = Graph(nodes_2, init_graph_2)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph_2, start_node="A")
print_result(previous_nodes, shortest_path, start_node="A", target_node="B")

