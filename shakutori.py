# 長さ nn の正の整数列 a1,a2,…,ana1,a2,…,an と整数 xx が与えられる。
# 整数列の連続する部分列で、その総和が xx 以下となるものを数え上げよ 
# (実際の出題は QQ 個のクエリがあって各クエリごとに xx が与えられる)。

# 入力受け取り
n,Q = list(map(int,input().split()))
A = list(map(int,input().split()))
X = list(map(int,input().split()))

# Q 回分のクエリを処理
for i in range(Q):
    # 各クエリ x
    x = X[i]

    # 合計値
    res = 0
    
    # 区間の左端 left で場合分け
    right = 0
    SUM = 0
    for left in range(n):
        # sum に a[right] を加えても大丈夫なら right を動かす
        while right < n and SUM+A[right] <= x:
            SUM += A[right]
            right += 1
        
        # break した状態で right は条件を満たす最大
        res += right - left

        # left をインクリメントする準備
        if right == left:
            right += 1
        else:
            SUM -= A[left]
    
    print(res)
