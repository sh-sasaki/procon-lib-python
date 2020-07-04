N = int(input())
A = list(map(int,input().split()))
W = int(input())
w_exists = False
for bit in range(1<<N):
    SUM = 0
    for i in range(N):
        if bit & (1<<i):
            SUM += A[i]
    if SUM == W:
        w_exists = True
if w_exists:
    print('Yes')
else:
    print('No')

S = int(input())
i = int(input())
#ビット S に i 番目のフラグが立っているかどうか
if S & (1<<i):
    pass
#ビットSにi番目のフラグが消えているかどうか
if not (S & (1<<i)):
    pass
#ビットSにi番目のフラグを立てる
S |= (1<<i)
#ビットSにi番目のフラグを消す
S &= ~(1<<i)
#ビットSに何個のフラグが立っているか
bin(S).count('1')
#ビットSにi番目のフラグを立てたもの
S | (1<<i)
#ビットSにi番目のフラグを消したもの
S & ~(1<<i)