### ソードアルゴリズム ###

### 1-1 ###
# バブルソート
N = int(input())
A = list(map(int, input().split()))

for _ in range (N):
    flag = False
    for i in range(N-1):
        if A[i] > A[i+1]:
            flag = True
            A[i], A[i+1] = A[i+1],A[i]

    if flag:
        print(*A)
    else:
        break
