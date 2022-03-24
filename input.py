###### 入力を受け取る（beta） ######

##### 複数の入力を受け取る #####

###2-3###
# 2 つの正の整数 A,B が空白区切りで入力されます。A と B のうち一の位が小さい方の値を出力してください。

# ただし、A と B の一の位は異なることが保証されています。

# 補足
# 整数の一の位はその数を 10 で割った余りと等しいです。
# たとえば 17 の一の位は 7 ですが、これは 17 を 10 で割った余りと一致します。

A,B = map(int,input().split())
if A%10 < B%10:
    print(A)
else:
    print(B)

###2-5###
# 3 つの整数 A,B,C が空白区切りで入力されます。3 つの整数の平均値を整数で出力してください。
#ただし、答えは整数になることが保証されています。

A,B,C = map(int,input().split())
print(round((A+B+C)/3))  ## ここでは、round() を使って結果を整数にする。

###2-6###
#4 つの正の整数 A,B,C,D が空白区切りで入力されます。4 つの整数の最大値を出力してください。

A,B,C,D = map(int,input().split())
list = [A,B,C,D]
print(max(list))

###2-7###
#2 つの文字列 S,T が改行区切りで入力されます。S と T が等しい文字列であるかを判定してください。

S = input()
T = input()  ## 改行が必要なため、S、Tを分けて入力する。
if S == T:
    print("Yes")
else:
    print("No")

###2-8###
#3 つの文字列 S, T, U が改行区切りで入力されます。U と T と S をこの順につなげた文字列を出力してください。

S = input()
T = input()
U = input()
print(U+T+S) ## +を使って文字列を結合する

### 2-10 ###
# 文字列 S が 1 行目に、2 つの正の整数 N,M が空白区切りで 2 行目に入力されます。 S の前からN番目の文字と、前からM番目の文字を入れ替えた文字列を出力してください。
# ただしここでは、文字列 S の先頭の文字は 1 文字目であるとします。

S = input()
N,M = map(int,input().split())
S_list = list(S)  ## Sをリストに変換する
tmp = S_list[N-1] ## 一時変数にS_list[N-1]を代入する
S_list[N-1] = S_list[M-1] ## 一時的にS_list[M-1]に代入する
S_list[M-1] = tmp
S = "".join(S_list) ## S_listを文字列に変換する
print(S)

##### たくさんの入力を受け取る #####
# 入力
# N
# A0 A1 ... AN-1 / S0 S1 ... SN-1

### 3-1 ###
# N 個の正の整数 A0 ,A1,…,AN−1が与えられます。N 個の整数の合計値を求めてください。

N = int(input()) # 入力を整数型として受け取る
A = list(map(int,input().split())) # 入力を整数型配列として受け取る
ans = 0  #答え
for item in A: #Aの各要素を足し合わせる
    ans += item
print(ans)

### 3-2 ###
# N 個の正の整数 A0 ,A1,…,AN−1が与えられます。N 個の整数を全て掛け合わせた値を求めてください。

N = int(input())
A = list(map(int,input().split()))
ans = 1
for item in A:
    ans *= item
print(ans)

### 3-3 ###
# N 個の正の整数 A0 ,A1,…,AN−1が与えられます。N 個の整数の一の位を改行区切りで順に出力してください。

N = int(input())
A = list(map(int,input().split()))
for item in A:
    print(item%10)

### 3-4 ###
# N 個の正の整数 A0 ,A1,…,AN−1が与えられます。 N個の整数のうち、3 の倍数であるものを改行区切りで全て出力してください。

N = int(input())
A = list(map(int,input().split()))
for item in A:
    if item%3 == 0:
        print(item)

### 3-5 ###
# N個の正の整数 A0 ,A1,…,AN−1が与えられます。N個の整数を後ろから改行区切りで出力してください。

N = int(input())
A = list(map(int,input().split()))
for item in reversed(A):
    print(item)

### 3-6 ###
# N個の正の整数 A0 ,A1,…,AN−1が与えられます。N個の正整数の平均値を求めてください。
# ただし、答えは小数点以下を切り捨てて出力してください。

N = int(input())
A = list(map(int,input().split()))
ans = 0
for item in A:
   ans += item
print(int(ans/N)) # int()を用いて小数点以下切り捨て

### 3-7 ###
# N個の正の整数 A0 ,A1,…,AN−1が与えられます。N 個の正整数の最小値を求め出力してください。

N = int(input())
A = list(map(int,input().split()))
print(min(A)) # min()を用いて最小値を求める

### 3-8 ###
# N個の文字列 S0 ,S1,…,SN−1が与えられます。N個の文字列を前からすべてつなげてできる文字列の長さを出力してください。

N = int(input())
A = [""] * N # N個の文字列を空文字列で初期化する
for i in range(N): # 0からN-1までRangeを作る
    A[i] = input()
ans = 0
for item in A: # Aの各要素の長さを足し合わせる
    ans += len(item)
print(ans)

### 3-9 ###
# N個の文字列 S0 ,S1,…,SN−1が与えられます。N 個の文字列の頭文字をつないでできる文字列を出力してください。

N = int(input())
A = [""] * N
for i in range(N):
    A[i] = input() #入力を文字列型配列として受け取る
ans = ""
for item in A:
    ans += item[0]
print(ans)

### 3-10 ###
# N個の文字列 S0 ,S1,…,SN−1が与えられます。N 個の文字列はすべて left または right のどちらかです。 N 個の文字列のうち、
# left の個数が多い場合は left を、
# right の個数が多い場合は right を、
# left と right の個数が等しい場合は same を出力してください。

N = int(input())
A = [""] * N
for i in range(N):
    A[i] = input()

count_left = 0
count_right = 0
for item in A:
    if item == "left":
        count_left += 1
    else:
        count_right += 1

if count_left > count_right:
    print("left")
elif count_left < count_right:
    print("right")
else:
    print("same")
