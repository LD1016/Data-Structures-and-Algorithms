def bfs(graph, vertex):
    visited = set()
    queue = []
    visited.add(vertex)
    queue.append(vertex)
    while len(queue) > 0:
        root = queue.pop(0)
        print(root)
        for node in graph[root]:
            if node not in visited:
                visited.add(node)
                queue.append(node)


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0', '4']),
         '3': set(['1', '4']),
         '4': set(['1', '2', '3'])}

bfs(graph, '0')
