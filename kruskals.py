from collections import defaultdict


class Graph:
    def __init__(self):
        self._graph_dict = defaultdict(list)

    def add_edge(self, v, u, w):
        self._graph_dict[v].append((u, w))
        self._graph_dict[u].append((v, w))

    def __len__(self):
        return len(self._graph_dict)

    def __iter__(self):
        return iter(self._graph_dict)

    def sorted(self):
        arr = [(v, u, w) for v in self._graph_dict for u, w in self._graph_dict[v]]
        return sorted(arr, key=lambda x: x[2])

def kruskals(graph):
    edges = []
    parents = list(range(len(graph)))
    ws = 0

    def find(v):
        if parents[v] == -1 or parents[v] == v:
            return v
        return find(parents[v])

    for v, u, w in graph.sorted():
        if find(v) != find(u):
            edges.append((v, u, w))
            parents[find(v)] = parents[find(u)] = max(find(v), find(u))
            ws += w
    
    return (ws, edges)
    
        




g = Graph()
g.add_edge(7, 6, 1)
g.add_edge(8, 2, 2)
g.add_edge(6, 5, 2)
g.add_edge(0, 1, 4)
g.add_edge(2, 5, 4)
g.add_edge(8, 6, 6)
g.add_edge(2, 3, 7)
g.add_edge(7, 8, 7)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(3, 4, 9)
g.add_edge(5, 4, 10)
g.add_edge(1, 7, 11)
g.add_edge(3, 5, 14)

print(kruskals(g))
