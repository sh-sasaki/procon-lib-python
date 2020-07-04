V,E = list(map(int,input().split()))
STD = [list(map(int,input().split())) for _ in range(E)]

D = [[float('inf')]*V for _ in range(V)]

for i in range(V):
    D[i][i] = 0

for std in STD:
    D[std[0]][std[1]] = std[2]

for k in range(V):
    for i in range(V):
        for j in range(V):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

for i in range(V):
    if D[i][i] < 0:
        print('NEGATIVE CYCLE')
        exit()

for d in D:
    print(*list(map(lambda x: str(x) if x != float('inf') else 'INF', d)))