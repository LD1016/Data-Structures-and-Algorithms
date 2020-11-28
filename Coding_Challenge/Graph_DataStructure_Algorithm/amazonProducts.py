from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited=None):
        if visited == None:
            visited = set()
        path = []

        def helper(v, visited, path):
            visited.add(v)
            path.insert(0, v)
            for node in self.graph[v]:
                if node not in visited:
                    helper(node, visited, path)
        helper(v, visited, path)
        return path


def largestItemAssociation(itemAssociation):
    result = []
    vertices = []
    g = Graph()
    for i in itemAssociation:
        u, v = i
        g.addEdge(int(u[-1]), int(v[-1]))
        if u not in vertices:
            vertices.append(int(u[-1]))
        if v not in vertices:
            vertices.append(int(v[-1]))
    for i in vertices:
        temp = g.dfs(i)
        if len(temp) > len(result):
            result = temp
    result = ['item'+str(i) for i in result]
    return result[::-1]


print(largestItemAssociation([['item1', 'item2'], ['item3', 'item4']]))
print(largestItemAssociation(
    [['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]))
print(largestItemAssociation([['item1', 'item2'], [
      'item4', 'item5'], ['item5', 'item6'], ['item6', 'item7']]))
