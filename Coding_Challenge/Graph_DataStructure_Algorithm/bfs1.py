def bfs(graph, node, visit=None):
    if visit is None:
        visit = set()
    visit.add(node)
    queue = [node]
    while len(queue) > 0:
        curr_node = queue.pop(0)
        print(curr_node)
        for i in graph[curr_node]:
            if i not in visit:
                visit.add(i)
                queue.append(i)


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0', '4']),
         '3': set(['1', '4']),
         '4': set(['1', '2', '3'])}

bfs(graph, '0')
