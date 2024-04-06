import typing


class Rerooting:
    def __init__(
        self,
        N: int,
        identity: typing.Any,
        merge: typing.Callable[[typing.Any, typing.Any], typing.Any],
        add_root: typing.Callable[[typing.Any, int], typing.Any],
    ) -> None:
        self.N = N
        self.edges = [[] for _ in range(N)]
        self.identity = identity
        self.merge = merge
        self.add_root = add_root
        self.dp = [[] for _ in range(N)]
        self.ans = [identity for _ in range(N)]

    def add_edge(self, u: int, v: int) -> None:
        self.edges[u].append(v)
        self.edges[v].append(u)

    def dfs1(self, v: int, p: int = -1) -> typing.Any:
        deg = len(self.edges[v])
        dp_cum = self.identity
        self.dp[v] = [self.identity] * deg

        for i, to in enumerate(self.edges[v]):
            if to == p:
                continue
            self.dp[v][i] = self.dfs1(to, v)
            dp_cum = self.merge(dp_cum, self.dp[v][i])

        return self.add_root(dp_cum, v)

    def dfs2(self, v: int, acc_par: typing.Any, p: int = -1) -> None:
        deg = len(self.edges[v])
        for i in range(deg):
            if self.edges[v][i] == p:
                self.dp[v][i] = acc_par

        prefix = [self.identity] * (deg + 1)
        suffix = [self.identity] * (deg + 1)
        for i in range(deg):
            prefix[i + 1] = self.merge(prefix[i], self.dp[v][i])
        for i in reversed(range(deg)):
            suffix[i] = self.merge(suffix[i + 1], self.dp[v][i])

        self.ans[v] = self.add_root(prefix[-1], v)

        for i, to in enumerate(self.edges[v]):
            if to == p:
                continue
            next_acc = self.merge(prefix[i], suffix[i + 1])
            next_acc = self.add_root(next_acc, to)
            self.dfs2(to, next_acc, v)

    def solve(self) -> typing.List[typing.Any]:
        self.dfs1(0)
        self.dfs2(0, self.identity)
        return self.ans


if __name__ == "__main__":
    identity = -1
    merge = lambda x, y: max(x, y)
    add_root = lambda x, v: x + 1

    n = 5
    rerooting = Rerooting(n, identity, merge, add_root)
    rerooting.add_edge(0, 1)
    rerooting.add_edge(0, 2)
    rerooting.add_edge(0, 3)
    rerooting.add_edge(0, 4)

    ans = rerooting.solve()
    print(ans)  # [1, 2, 2, 2, 2]
