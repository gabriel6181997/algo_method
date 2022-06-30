###動的計画法（DP）###


# Q1-1 数字の列
N, X, Y = map(int,input().split())

# 計算の舞台となる配列を宣言
A = [0] * N

# 初期値を定める
A[0], A[1] = X,Y

for i in range(2,N):
    A[i] = (A[i-1] + A[i-2])%100

print(A[-1])

# Q1-2 マスの移動（１）
N = int(input())
A = list(map(int,input().split()))

T = [0]*N

T[1] = A[1]

for i in range(2,N):
    T[i] = min(T[i-1]+A[i], T[i-2]+A[i]*2)

print(T[-1])


# Q1-3 階段ののぼり方
N = int(input())

F = [0] * (N+1)

F[0], F[1] = 1,1

for i in range(2,N+1):
    F[i] = F[i-2] + F[i-1]

print(F[N])


# Q1-4 タイルの敷き詰め
N = int(input())

T = [0] * (N+1)

T[0] = 1

for i in range(1,N+1):
    if i-1 >= 0:
        T[i] += T[i-1]
    if i-2 >= 0:
        T[i] += T[i-2]
    if i-3 >= 0:
        T[i] += T[i-3]
print(T[N])

# Q1-5 マスの移動（２）(理解不可能)
INF = 1000000

N, M = map(int,input().split())
A = list(map(int, input().split()))

T = [INF] * N

T[0] = 0

for i in range(1,N):
    for j in range(1,M+1):
        if i-j >= 0:
            T[i] = min(T[i], T[i-j]+A[i]*j)
print(T[-1])

# Q1-6 すごろく(理解不可能)
N, M = map(int,input().split())
D = list(map(int,input().split()))

dp = [False] * (N+1)

dp[0] = True

for i in range(1, N+1):
    for j in range(M):
        if i - D[j] >= 0 and dp[i-D[j]]:
            dp[i] = True

print('Yes' if dp[N] else 'No')

