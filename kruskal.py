from union_find import UnionFind

V,E = list(map(int,input().split()))
STW = sorted([list(map(int,input().split())) for _ in range(E)],key=lambda x: x[2])

union_find = UnionFind(V+1)
ans = 0
for s,t,w in STW:
    if not union_find.same(s,t):
        ans += w
        union_find.unite(s,t)
