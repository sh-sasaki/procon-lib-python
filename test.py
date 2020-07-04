class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [1]*n
    
    def root(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = y = self.root(self.p[x])
        return y
    
    def unite(self, x, y):
        px = self.root(x); py = self.root(y)
        if px == py:
            return 0
        rx = self.rank[px]; ry = self.rank[py]
        if ry < rx:
            self.p[py] = px
        elif rx < ry:
            self.p[px] = py
        else:
            self.p[py] = px
            self.rank[px] += 1
        return 1

    def same(self, x, y):
        px = self.root(x); py = self.root(y)
        return px == py

V,E = list(map(int,input().split()))
STW = sorted([list(map(int,input().split())) for _ in range(E)],key=lambda x: x[2])

union_find = UnionFind(V+1)
ans = 0
for s,t,w in STW:
    if not union_find.same(s,t):
        ans += w
        union_find.unite(s,t)