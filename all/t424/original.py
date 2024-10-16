# Partially generated by ChatGPT

class Graph:
    def __init__(self):
        self.nodes = {}
        self.index2node = []
        self.graph = []
        self.prev = []

    def add_node(self, node):
        if node in self.nodes:
            return
        self.index2node.append(node)
        self.nodes[node] = len(self.nodes)
        for row in self.graph:
            row.append(float('inf'))
        new_row = [float('inf')] * len(self.nodes)
        new_row[-1] = 0
        self.graph.append(new_row)
        for row in self.prev:
            row.append(None)
        new_row = [None] * len(self.nodes)
        new_row[-1] = len(self.nodes)-1
        self.prev.append(new_row)

    def update_distance(self, node1, node2, distance):
        assert node1 in self.nodes and node2 in self.nodes

        index1 = self.nodes[node1]
        index2 = self.nodes[node2]

        self.graph[index1][index2] = distance
        self.graph[index2][index1] = distance

        self.prev[index1][index2] = index1
        self.prev[index2][index1] = index2

    def get_distance(self, node1, node2):
        assert node1 in self.nodes and node2 in self.nodes

        index1 = self.nodes[node1]
        index2 = self.nodes[node2]

        return self.graph[index1][index2]

    def update_distances(self):
        num_nodes = len(self.graph)
        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if self.graph[i][k] + self.graph[k][j] < self.graph[i][j]:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]
                        self.prev[i][j] = self.prev[k][j]

    # XXX: I really feel it's wrong, but it works for my case
    def update_distances_for_node(self, node):
        index = self.nodes[node]
        num_nodes = len(self.graph)
        for k in range(num_nodes):
            for i in range(num_nodes):
                if self.graph[index][k] + self.graph[k][i] < self.graph[index][i]:
                    self.graph[index][i] = self.graph[index][k] + self.graph[k][i]
                    self.prev[index][i] = self.prev[k][i]
                if self.graph[i][k] + self.graph[k][index] < self.graph[i][index]:
                    self.graph[i][index] = self.graph[i][k] + self.graph[k][index]
                    self.prev[i][index] = self.prev[k][index]

    def shortest_path(self, source, destination):
        assert source in self.nodes and destination in self.nodes

        source_index = self.nodes[source]
        destination_index = self.nodes[destination]

        assert self.graph[source_index][destination_index] != float('inf')
        assert self.prev[source_index][destination_index] is not None

        path = [self.index2node[destination_index]]
        while source_index != destination_index:
            destination_index = self.prev[source_index][destination_index]
            path.insert(0, self.index2node[destination_index])

        return path

    def print_shortest_distances(self):
        for node1, index1 in self.nodes.items():
            for node2, index2 in self.nodes.items():
                if self.graph[index1][index2] == float('inf'):
                    print("INF", end="\t")
                else:
                    print(self.graph[index1][index2], end="\t")
            print()

        print(self.prev)