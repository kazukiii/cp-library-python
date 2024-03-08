class LCA:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.lg = n.bit_length()
        self.parent = [[-1] * n for _ in range(self.lg)]
        self.depth = [0] * n
        self.visited = [False] * n
        self.dfs(0, 0)
        self.preprocess()

    def dfs(self, v, p):
        self.visited[v] = True
        self.parent[0][v] = p
        for u in self.edges[v]:
            if not self.visited[u]:
                self.depth[u] = self.depth[v] + 1
                self.dfs(u, v)

    def preprocess(self):
        for i in range(1, self.lg):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def query(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]

        for i in range(self.lg):
            if diff & (1 << i):
                u = self.parent[i][u]

        if u == v:
            return u

        for i in reversed(range(self.lg)):
            if self.parent[i][u] != self.parent[i][v]:
                u = self.parent[i][u]
                v = self.parent[i][v]

        return self.parent[0][u]


if __name__ == "__main__":
    graph = [[1, 2], [0], [0, 3, 4], [2], [2]]
    lca = LCA(5, graph)
    assert lca.query(0, 1) == 0
    assert lca.query(1, 2) == 0
    assert lca.query(3, 4) == 2
