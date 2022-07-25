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

