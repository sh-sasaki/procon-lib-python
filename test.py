V,E = list(map(int,input().split()))
STD = [list(map(int,input().split())) for _ in range(E)]

D = [[float('inf')]*V for _ in range(V)]

for i in range(V):
    D[i][i] = 0

for std in STD:
    D[std[0]-1][std[1]-1] = std[2]
    D[std[1]-1][std[0]-1] = std[2]

for k in range(V):
    for i in range(V):
        for j in range(V):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

MIN = float('inf')
for d in D:
    MIN = min(max(d),MIN)
print(MIN)