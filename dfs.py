import sys
sys.setrecursionlimit(10**7)

N = int(input())
UKV = [list(map(int,input().split())) for _ in range(N)]

seen = [False]*N
first_order = [-1]*N
last_order = [-1]*N
first_num = 0
last_num = 0
def dfs(G, v):
    global seen
    global first_order
    global last_order
    global first_num
    global last_num
    seen[v] = True
    first_num += 1
    first_order[v] = first_num
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)
    last_num += 1
    last_order[v] = last_num

G = {}
for ukv in UKV:
    G[ukv[0]] = sorted(ukv[2:])

for i in range(N):
    if seen[i]:
        continue
    dfs(G, i)

for i in range(N):
    print(i,first_order[i],last_order[i])


def dfs_rec():
    W,H = list(map(int,input().split()))
    if W == 0 and H == 0:
        exit()
    C = [list(map(int,input().split())) for _ in range(H)]
    D = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]
    
    def dfs(C, x, y):
        C[y][x] = 2
        for d in D:
            if x+d[0] < 0 or x+d[0] > W-1 or y+d[1] < 0 or y+d[1] > H-1:
                continue
            if C[y+d[1]][x+d[0]] == 0 or C[y+d[1]][x+d[0]] == 2:
                continue
            dfs(C, x+d[0], y+d[1])
    
    count = 0
    for w in range(W):
        for h in range(H):
            if C[h][w] == 0 or C[h][w] == 2:
                continue
            dfs(C, w, h)
            count += 1
    
    print(count)

while True:
    dfs_rec()