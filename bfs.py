import collections

N = int(input())
UKV = [list(map(int,input().split())) for _ in range(N)]

dist = [-1]*N
que = collections.deque()

G = [[]]*N
for ukv in UKV:
    G[ukv[0]-1] = sorted(ukv[2:])

dist[0] = 0
que.append(1)

while len(que) != 0:
    v = que.popleft()
    for nv in G[v-1]:
        if dist[nv-1] != -1:
            continue
        dist[nv-1] = dist[v-1] + 1
        que.append(nv)

for i,d in enumerate(dist):
    print(i+1, d)


import collections
 
R,C = list(map(int,input().split()))
sy,sx = list(map(int,input().split()))
sy,sx = sy-1,sx-1
gy,gx = list(map(int,input().split()))
gy,gx = gy-1,gx-1
CC = [list(input()) for _ in range(R)]
 
que = collections.deque()
que.append([sy,sx])
 
d = [[float('inf') for _ in range(C)] for _ in range(R)]
d[sy][sx] = 0
 
while len(que) != 0:
    y,x = que.popleft()
    if y == gy and x == gx:
        print(d[y][x])
        exit()
    for direct in [[1,0],[-1,0],[0,1],[0,-1]]:
        if CC[y+direct[0]][x+direct[1]] != '#':
            d[y+direct[0]][x+direct[1]] = d[y][x]+1
            CC[y+direct[0]][x+direct[1]] = '#'
            que.append([y+direct[0], x+direct[1]])