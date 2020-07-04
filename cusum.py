N = int(input())
A = list(map(int,input().split()))
S = [0]*(N+1)
S[0] = 0
for i in range(N):
    S[i+1] = S[i]+A[i]
for k in range(N):
    MAX = 0
    for i in range(N-k):
        MAX = max(MAX,S[i+k+1]-S[i])
    print(MAX)