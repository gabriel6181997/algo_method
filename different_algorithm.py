##### さまざまなアルゴリズム設計技法 #####

### Q4-3. フィボナッチ数列 (再帰-1)
import sys
sys.setrecursionlimit(10**6)

def func(N):
    if N == 0:
        return 0
    if N == 1:
        return 1

    return func(N-1)+func(N-2)

N = int(input())

print(func(N))


### Q4-4. フィボナッチ数列 (再帰-2)
import sys
sys.setrecursionlimit(10**6)

def func(N):
    print(f"func({N})を計算します。")
    if memo[N] != -1:
      return memo[N]
    if N == 0:
        memo[N] = 0
    elif N == 1:
        memo[N] = 1
    else:
        memo[N] = func(N-1)+func(N-2)
    return memo[N]

N = int(input())
memo = [-1] * (N+1)

print(func(N))

