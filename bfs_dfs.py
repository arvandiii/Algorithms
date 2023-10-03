from collections import defaultdict

class Graph:
    def __init__(self):
        self._graph_dict = defaultdict(list)
        
    def add_edge(self, u, v):
        self._graph_dict[u].append(v)
        self._graph_dict[v].append(u)

    def __len__(self):
        return len(self._graph_dict)
    
    def neighbors(self, node):
        return self._graph_dict[node]

def bfs(graph, start=0):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbour in graph.neighbors(node):
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

def dfs(graph, start=0):
    visited = [False] * len(graph)
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        print(node, end=' ')

        for neighbour in graph.neighbors(node):
            if not visited[neighbour]:
                stack.append(neighbour)
                visited[neighbour] = True
        

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 6)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(5, 3)


print('bfs:')
bfs(g, 5)
print('\ndfs:')
dfs(g, 0)