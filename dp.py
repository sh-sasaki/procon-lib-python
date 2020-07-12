#フィボナッチ数
N = int(input())
dp = {0:1,1:1}
for i in range(1,N):
    dp[i+1] = dp[i]+dp[i-1]
print(dp[N])

#ナップザック問題
N,W = list(map(int,input().split()))
VW = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if VW[i][1] <= w:
            # i番目までの品物の中から重さがwを超えないように選んだときの、価値の総和の最大値
            dp[i+1][w] = max(dp[i][w-VW[i][1]]+VW[i][0],dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]

print(dp[N][W])