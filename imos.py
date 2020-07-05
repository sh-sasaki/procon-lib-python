N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
T = [0]*(1000001)
NL = [0]*(1000001)
for a,b in AB:
    T[a] += 1
    if b+1 < 1000001:
        T[b+1] -= 1
for i in range(1,1000001):
    T[i] += T[i-1]
print(max(T))
