"""
Given two words A and B, and a dictionary, C, find the length of 
shortest transformation sequence from A to B, such that:
You must change exactly one character in every transformation.
Each intermediate word must exist in the dictionary.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Input Format:
The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains an array of strings, C.

Output Format:
Return an integer representing the minimum number of steps required to change string A to string B.
Constraints:

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5e3

Example :
Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log"]

Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -cd> "dog" -> "cog"
"""


class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        graph = Graph()
        for node in C:
            graph.addVertex(node)
        for node1 in C:
            for node2 in C:
                different = 0
                for i in range(len(node1)):
                    if node1[i] != node2[i]:
                        different += 1
                if different == 1:
                    graph.addEdge(node1, node2)
        result = 10000
        # graph.showConnections()
        # for i in range(graph.numberOfNodes):
        #     result = min(result, graph.bfs(A, B))
        return graph.bfs(A, B)


class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)

    def showConnections(self):
        for x in self.adjacentList:
            print(x, end='--->')
            for i in self.adjacentList[x]:
                print(i, end=' ')
            print()

    def bfs(self, node1, node2):
        if node1 == node2:
            return 0
        visited = dict()
        queue = []
        visited[node1] = 0
        queue.append(node1)
        # step = 0
        while len(queue) > 0:
            root = queue.pop(0)
            # print(root)
            if root == node2:
                # print(node2)
                return visited[root] + 1
            for node in self.adjacentList[root]:
                if node not in visited:
                    # print(node, step)
                    visited[node] = visited[root] + 1
                    queue.append(node)
            # step += 1
            # print(step)
        # print(step)
        return 0


test = Solution()
print(test.solve("ymain", "oecij", ["ymann", "yycrj", "oecij", "ymcnj",
                                    "yzcrj", "yycij", "xecij", "yecij", "ymanj", "yzcnj", "ymain"]))
print(test.solve("hit", "cog", ["hit", "hot",
                                "dot", "dog", "lot", "log", "cog"]))
