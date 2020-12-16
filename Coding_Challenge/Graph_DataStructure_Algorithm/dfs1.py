def dfs(graph, node, visit=None):
    if visit is None:
        visit = set()
    visit.add(node)
    print(node)
    for i in graph[node]:
        if i not in visit:
            dfs(graph, i, visit)


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0', '4']),
         '3': set(['1', '4']),
         '4': set(['1', '2', '3'])}

dfs(graph, '2')
