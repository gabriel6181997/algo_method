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

### 1-2 ###
# 選択ソート

N = int(input())
A = list(map(int,input().split()))

for k in range(N-1):
    # 未ソートの要素のうち最小値がある位置を求める
    min_element_index = A[k:].index(min(A[k:])) + k
    # 未ソートの要素の先頭 A[k] と最小値を入れ替え、
    # 次のループでは A[0]...A[k] をソート済みとみなす
    A[k], A[min_element_index] = A[min_element_index], A[k]

    # 現時点での配列の中身を出力する
    print(*A)

### 1-3 ###
# 挿入ソート
N = int(input())
A = list(map(int,input().split()))

for k in range(1,N):
    while k and A[k-1] > A[k]:
        A[k-1],A[k] = A[k], A[k-1]
        k -= 1

    print(*A)

### 1-4 ###
# クイックソード

N = int(input())
A = list(map(int,input().split()))

def quick_sort(v):
    if len(v) == 0:
        return []

    X = len(v)//2
    L,R = [],[]
    for i, element in enumerate(v):
        if i == X:
            continue
        if element < v[X]:
            L.append(element)
        else:
            R.append(element)

    L = quick_sort(L)
    R = quick_sort(R)

    L.append(v[X])
    L.extend(R)
    return L

A = quick_sort(A)

print(*A)

### 1-5 ###
# 乱択クイックソート

from distutils.command.build import build
import random

N = int(input())
A = list(map(int, input().split()))

# クイックソート本体
def quick_sort(v):
    # 配列が空の場合は何も起こらない
    if len(v) == 0:
        return []

    # v[X] の値を軸に配列を分割する
    X = random.randrange(len(v))
    L, R = [], []
    for i, element in enumerate(v):
        if i == X:
            continue
        if element == v[X]:
            # 等確率で L または R に振り分ける
            if random.randrange(2):
                L.append(element)
            else:
                R.append(element)
        elif element < v[X]:
            L.append(element)
        else:
            R.append(element)

    # L, R を再帰的にソートする
    L = quick_sort(L)
    R = quick_sort(R)

    # L, v[X], R をこの順につなげ、もとの配列を更新する
    L.append(v[X])
    L.extend(R)
    return L

# クイックソート
A = quick_sort(A)

# 配列の中身を出力する
print(*A)


### 1-6 ###
# マージソート

from collections import deque

N = int(input())
A = list(map(int,input().split()))

def merge_sort(v):
    if len(v) == 0:
        return

    x = len(v)//2
    L,R = v[:x],v[x:]

    if len(L)>=2: L = merge_sort(L)
    if len(R)>=2: R = merge_sort(R)

    dq = deque()
    for l in L: dq.append(l)
    for r in reversed(R): dq.append(r)
    B = []
    while len(dq):
        if dq[0] <= dq[-1]:
            B.append(dq.popleft())
        else:
            B.append(dq.pop())
    return B

A = merge_sort(A)

print(*A)

## Information related to deque
# https://note.nkmk.me/python-collections-deque/


### 1-7 ###
# ヒープソートの準備

N = int(input())
A = list(map(int,input().split()))

def build_heap(v):
    for x in range(len(v)//2, -1, -1):
        k = x
        while True:
            left = v[2*k+1] if 2*k+1 < len(v) else 0
            right = v[2*k+2] if 2*k+2 < len(v) else 0
            if left == 0 and right == 0:
                break
            elif v[k] >= left and v[k] >= right:
                break
            elif left >= right:
                v[k], v[2*k+1] = v[2*k+1], v[k]
                k = 2*k+1
            else:
                v[k], v[2*k+2] = v[2*k+2], v[k]
                k = 2*k+2

build_heap(A)

print(*A)

### 1-8 ###
# ヒープソート

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 要素の整理
def align_elements(v, start_pos, end_pos):
    k = start_pos
    while True:
        # ノードが存在しない場合は０を仮置きする
        left = v[2*k+1] if 2*k+1 < end_pos else 0
        right = v[2*k+2] if 2*k+2 < end_pos else 0
        if left == 0 and right == 0: #子ノードが存在しない
            break
        elif v[k]>= left and v[k]>= right: #最大値がv[k]
            break
        elif left >= right: #最大値がv[2*k+1]
            v[k], v[2*k+1] = v[2*k+1], v[k]
            k = 2*k+1
        else: #最大値がv[2*k+2]
            v[k], v[2*k+2] = v[2*k+2], v[k]
            k = 2*k+2

# 二分ヒープの構築
def build_heap(v):
    for x in range(len(v)//2, -1, -1):
        align_elements(v,x,len(v))

# ヒープの根を削除する（根の要素をソート済の位置に移動させる）
def delete_root(v,end_pos):
    v[0],v[end_pos] = v[end_pos], v[0]
    align_elements(v,0,end_pos)

# 二分ヒープの構築
build_heap(A)

# ソートを実装に行う
for i in range(N-1,0,-1):
    delete_root(A,i)
    # i=M の操作が終了した時点での配列の様子を出力
    if i==M:
        print(*A)

# 最終的な配列Aの様子を出力
print(*A)

### 1-9 ###
# バゲットソート

N = int(input())
A = list(map(int, input().split()))

X = N + 1
num = [0] * X
for a in A:
    num[a] += 1
acc = [0] * X
for idx, count in enumerate(num):
    if idx == 0:
        acc[idx] = count
    else:
        acc[idx] = acc[idx-1] + count
B = [0] * N
for a in A:
    acc[a] -= 1
    B[acc[a]] = a

print(*B)

### 2-1 ###
# 中央値

N = int(input())
A = list(map(int,input().split()))

A.sort()

if N%2 == 1:
    print(A[(N-1)//2])
else:
    print((A[N//2-1]+A[N//2])/2)

### 2-2 ###
# 各要素の平均

# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

# A をソート
A.sort()

# それぞれ答える
for x in X:
    print(A[x])

### 2-3 ###
# 総和の最大値

N,K = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse = True)

print(sum(A[0:K]))

### 2-4 ###
# 差の最小値

N,K = map(int,input().split())
A = list(map(int, input().split()))

A.sort()

result = 2 ** 60

for i in range(N-K+1):
    diff = A[i+K-1] - A[i]
    result = min(result, diff)

print(result)

### 2-5 ###
# ごはんを買う

N,K = map(int,input().split())
S = [tuple(map(int, input().split())) for i in range(N)]

S.sort()

res = 0

for(A,B) in S:
    num = min(K,B)
    K -= num
    res += A * num

print(res)
