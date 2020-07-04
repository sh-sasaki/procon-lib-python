import heapq
V,E,r = list(map(int,input().split()))
STD = [list(map(int,input().split())) for _ in range(E)]

G = {i:[] for i in range(V)}
for std in STD:
    G[std[0]].append([std[1],std[2]])

dist = [float('inf')] * V
que = [(0, r)]
dist[r] = 0
while que:
    c, v = heapq.heappop(que)
    if dist[v] < c:
        continue
    for t, cost in G[v]:
        if dist[v] + cost < dist[t]:
            dist[t] = dist[v] + cost
            heapq.heappush(que, (dist[t], t))
for cost in dist:
    if cost == float('inf'):
        print('INF')
    else:
        print(cost)