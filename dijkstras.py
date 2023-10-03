from collections import defaultdict


class WGraph:
    _graph = {}

    def __init__(self):
        self._graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self._graph[u].append((v, w))
        self._graph[v].append((u, w))

    def dijkstra(self, start):
        dist = [float('inf')] * len(self._graph)
        path = [None] * len(self._graph)
        visited = [False] * len(self._graph)

        dist[start] = 0
        path[start] = start
        queue = [start]

        while queue:
            node = queue.pop(0)
            visited[node] = True

            for neighbour, weight in self._graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    if dist[neighbour] > dist[node] + weight:
                        path[neighbour] = node
                        dist[neighbour] = dist[node] + weight

        for i in range(1, len(self._graph)):
            current = i
            print(f'path from {start} to {current}:', end=' ')
            path_str = ''
            while current != start:
                path_str = f'{current} {path_str}'
                current = path[current]

            print(path_str, '-', dist[i])


g = WGraph()
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)
g.dijkstra(0)
