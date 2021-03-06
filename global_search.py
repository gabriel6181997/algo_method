###### 全探索 ######

#### 配列の全検索 ####

### 1-1 ###
# N 個の整数 A0 ,A1,…,AN−1​が与えられます (整数の個数 N も入力として与えられます)。
# N 個の整数の中に、整数 V があるかどうかを判定するプログラムを作成してください。
# 入力
#N V
#A0 ,A1,…,AN−1

N, V = map(int,input().split())
data = map(int,input().split())

# 線形探索
flag = False  # 探索結果を格納するフラグを立てる（初期値をFalseにする）
for d in data:
    if d == V:
        flag = True

# 答えを出力する
if flag:
    print("Yes")
else:
    print("No")

### 1-2 ###
# N 個の整数 A0 ,A1,…,AN−1​が与えられます。
# N 個の整数の中に整数 V が何個あるかを数えるプログラムを作成してください。
# 入力
#N V
#A0 ,A1,…,AN−1

N, V = map(int,input().split())
data = map(int, input().split())

flag = 0
for d in data:
    if d == V:
        flag += 1

print(flag)

### 1-3 ###
# N 個の整数 A0 ,A1,…,AN−1​が与えられます。
# N 個の整数の中に 0 より大きいものが何個あるかを数えるプログラムを作成してください。

N = int(input())
data = map(int,input().split())

flag = 0
for item in data:
    if item > 0:
        flag += 1

print(flag)

### 1-4 ###
# N 個の整数 A0 ,A1,…,AN−1​が与えられます。
# N 個の整数の中で 最も右にある V は前から何番目にあるかを調べるプログラムを作成してください。
# ただし、V が存在しない場合はそのことを報告してください。 また、N 個の整数のうち先頭の要素 A0を、前から 0 番目であると数えることとします。

N, V = map(int,input().split())
A = list(map(int,input().split()))

pos = -1
for i in range(N):
    if A[i] == V:
        pos = i

print(pos)

### 1-5 ###
# N 個の整数 A0 ,A1,…,AN−1​が与えられます。
# 次の条件を満たす i の個数を調べるプログラムを作成してください。
# ・i は 1 以上 N−1 以下の整数
# ・Aiは Ai−1よりも大きい

N = int(input())
A = list(map(int,input().split()))

count = 0
for i in range(1,N): # i は 1 以上 N−1 以下の整数なので、上限も下限も設ける必要がある
    if A[i-1] < A[i]:
        count += 1

print(count)

### 1-7 ###
# N 個の互いに相異なる整数 A0 ,A1,…,AN−1​が与えられます。
# N 個の整数の中で一番大きいものは前から何番目にあるかを調べるプログラムを作成してください。
# ただし、N 個の整数のうちの先頭の整数 A0は、前から 0 番目であると考えることとします。

N = int(input())
A = list(map(int,input().split()))

pos = -1
for i in range(N):
    if A[i] == max(A):
        pos = i

print(pos)

### 1-9 ###
#N 個の1以上9以下の整数 A0 ,A1,…,AN−1​が与えられます。
#N 個の整数に含まれる 1,2,…,9 の個数をそれぞれ求めるプログラムを作成してください。

N = int(input())
A = list(map(int,input().split()))

count = [0] * 9 # 長さ 9 の配列 count を用意し、 0 で初期化する
for x in A:
    count[x-1] += 1 #i を 0 から N−1 まで以下を繰り返す。count[A[i]] の値を 1 だけ増やす

for x in count:
    print(x)

### 1-10 ###
# N 個の1以上9以下の整数 A0 ,A1,…,AN−1​が与えられます。
# N 個の整数の中に一番多く出てくる数字を求めるプログラムを作成してください。 ただし、答えは一つに定まることが保証されているものとします。

N = int(input())
A = list(map(int,input().split()))
most_common = max(A, key=A.count)
print(most_common)

#### 数字の全探索 ####

### 2-1 ###
# 1 以上 N 以下の整数のうち、2 でも 3 でも 5 でも割り切れない数の個数を数えるプログラムを作成してください。

N = int(input())

count = 0

for i in range (1, N+1):  #1からN+1未満(N以下)の整数iを順に調べる処理
    if i%2 != 0 and i%3 !=0 and i%5 !=0:
        count += 1

print(count)

### 2-2 ###
# N の約数の個数を数えるプログラムを作成してください。
#ただし N の約数とは「 N を割り切ることのできる 1 以上の整数」のことです。

N = int(input())

count = 0

for i in range (1,N+1):
    if N%i == 0:
        count += 1

print(count)

### 2-3 ###
#整数 N が素数かどうかを判定するプログラムを作成してください。
#ただし次の条件を満たすとき「 N は素数である」と言います。
#・N は 2 以上の整数である
#・N を割り切ることのできる 1 より大きい整数は N のみである

N = int(input())

if N == 1:  # 1 は素数ではないため
    print("No")
else:
    is_prime = True
    for i in range (2,N): #2以上N-1以下の数でNを順番に割る
        if N%i == 0:
            is_prime = False

    if is_prime:
       print("Yes")
    else:
       print("No")

### 2-4 ###
# 整数 A と B の最大公約数を出力するプログラムを作成してください。
# ただし次の条件を満たすとき「 X は A と B の最大公約数である」と言います。
# 条件：X は A も B も割り切る 1 以上の整数の中で最大のものである

A, B = map(int,input().split())

ans = 0
for i in range(1,min(A,B)+1):
    if A % i == 0 and B % i == 0:
        ans = i

print(ans)

### 2-5 ###
# 正の整数 N が与えられます。 1 以上 N 以下の整数 i について、次の問題に答えてください。

#・ i が 3 でも 5 でも割り切れるならば FizzBuzz を出力し、
#・それ以外で i が 3 で割り切れるならば Fizz を出力し、
#・それ以外で i が 5 で割り切れるならば Buzz を出力し、
#・i がどちらでも割り切れないならば i 自身を出力してください。

N = int(input())

for i in range(1,N+1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)


### 文字列の全探索 ###

### 3-1 ###
# 英小文字からなる文字列 S と、英小文字 c が与えられます。
# 文字列 S の中に c が含まれるかどうかを答えるプログラムを作成してください。

S = input()
c = input()

N = len(S)

flag = False
for i in range(N):
    if S[i] == c:
        flag = True

if flag:
    print("Yes")
else:
    print("No")


### 3-2 ###
# 英小文字からなる文字列 S が与えられます。
# 文字列 S が回文かどうかを判定するプログラムを作成してください。 なお文字列 S が回文であるとは、S を逆から読んでも S になることを言います。

S = input()

w = "" #空の文字列を用意する
for i in S:
    w = i + w # iをwに代入していく

if S == w:
    print("Yes")
else:
    print("No")


### 3-3 ###
# 英小文字からなる文字列 S が与えられます。
# 文字列 S 中に「連続する 2 文字が同じ文字である箇所」が何個あるかを答えるプログラムを作成してください。

S = input()

N = len(S)

count = 0
for i in range (N-1): #i を 0 から N−2 まで以下を繰り返す
    if S[i] == S[i+1]:
       count += 1

print(count)

### 3-4 ###
#英小文字からなる長さ N の文字列 S, T が与えられます。
#文字列 S の何文字かを書き換えることで、文字列 T に一致させたいものとします。 置き換える必要のある文字数を答えるプログラムを作成してください。

N = int(input())
S = input()
T = input()

count = 0
for i in range(N):
   if S[i] != T[i]:
       count += 1

print(count)

### 3-5 ###
# 英小文字からなる文字列 S, T が与えられます。
# 文字列 S の連続する文字列を抜き出すことで、 文字列 T と一致させることができるかどうかを答えるプログラムを作成してください。

S = input()
T = input()

N = len(S)
M = len(T)

flag = False
for i in range(N-M+1): #0からN-Mまで以下を繰り返す
    if S[i:i+M] == T: #M文字分の文字列を取り出して、Tと比較する
        flag = True

if flag:
    print("Yes")
else:
    print("No")

### 二重ループの全探索 ###

### 4-1 ###
# N 個の整数 A0 ,A1,…,AN−1が与えられます。
# N 個の整数の中に素数がいくつあるか調べるプログラムを作成してください。

N = int(input())
A = list(map(int,input().split()))

counter = 0
for x in A:
    is_prime = True
    if x == 1:
        is_prime = False
    else:
        for i in range(2,x):
            if x%i == 0:
                is_prime = False
    if is_prime:
        counter += 1

print(counter)

### 4-2 ###
# 1 以上の整数 N, K が与えられます。
# 1 以上 N 以下の整数の中で約数をちょうど K 個持つ数の個数を調べるプログラムを作成してください。

N, K = map(int, input().split())

count = 0
for x in range(1, N+1):
    yaku = 0
    for i in range(1, x+1):
        if x%i == 0:
            yaku += 1
    if yaku == K:
        count += 1

print(count)

### 4-3 ###
# 整数 X を文字列としてみると回文になっているとき、「X は回文数である」と呼ぶことにします。
# 整数 L, R が与えられるので、L 以上 R 以下の整数の中に回文数がいくつあるか数えるプログラムを作成してください。

L, R = map(int, input().split())

count = 0
for x in range(L, R+1):
    S = str(x)
    flag = True
    N = len(S)
    for i in range(N):
        if S[i] != S[(N-1)-i]:
            flag = False
    if flag:
        count += 1

print(count)

### 4-4 ###
# 英小文字からなる文字列 S が与えられます。
# 文字列 S に使われている英小文字の種類数を答えるプログラムを作成してください。

S = input()
N = len(S)

count = 0
for x in range(ord('a'), ord('z') + 1): # ord()は文字を数値(unicode)に変換する関数
     c = chr(x) #chr()はunicode x を示す文字を返す
     # S に c が含まれるかを調べる
     flag = False
     for i in range(N):
        if S[i] == c:
            flag = True
     if flag:
        count += 1

print(count)

### 4-5 ###
# 英小文字からなる N個の文字列 S0 ,S1,…,SN−1が与えられます。
# N 個の文字列のうち回文の個数を数えるプログラムを作成してください。

def is_palindrome(x):
      flag = True
      N = len(x)
      for i in range (N):
        if x[i] != x[(N-1)-i]:
            flag = False
      return flag


N = int(input())
S = [input() for _ in range(N)]

count = 0
for x in S:
    if is_palindrome(x):
        count += 1

print(count)

### 複数の配列の全探索 ###

### 5-1 ###
# N 個の整数 A0,A1,…,AN−1と M 個の整数 B0,B1,…,BM−1が与えられます。
# 次の条件を満たす組 (i,j) の個数を答えるプログラムを作成してください。
#・i は 0 以上 N−1 以下の整数
#・j は 0 以上 M−1 以下の整数
#・Ai>Bj

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

counter = 0
for x in A:
    for y in B:
        if x > y:
            counter += 1

print(counter)

### 5-2 ###
# N 個の整数 A0,A1,…,AN−1と M 個の整数 B0,B1,…,BM−1と整数 K が与えられます。
# 次の条件を満たす組 (i,j) の個数を答えるプログラムを作成してください。
# i は 0 以上 N−1 以下の整数
# j は 0 以上 M−1 以下の整数
# Ai+Bj =K

N, M, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

counter = 0
for x in A:
    for y in B:
        if x + y == K:
            counter += 1

print(counter)

### 5-3 ###
# X 個の整数 A0,A1,…,AX−1と、 Y 個の整数 B0,B1 ,…,BY−1と、 Z 個の整数 C0 ,C1,…,CZ−1が与えられます。
# 次の条件を満たす組 (i,j,k) の個数を答えるプログラムを作成してください。
# ・i は 0 以上 X−1 以下の整数
# ・j は 0 以上 Y−1 以下の整数
# ・k は 0 以上 Z−1 以下の整数
# ・Ai+Bj=Ck

X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

counter = 0
for x in A:
    for y in B:
        for z  in C:
            if x+y == z:
                counter += 1

print(counter)

#### ペアの全探索 ####

### 6-1 ###
# N 個の整数 A0,A1,…,AN−1と整数 K が与えられます。
# これらの N 個の整数から、和が K 以下となるように 2 つの数を選ぶ方法は何通りあるか求めるプログラムを作成してください。
# ただし選んだ 2 つの整数の添字 (Aiの i) が等しくなってはいけないものとします。

N, K = map(int,input().split())
A = list(map(int,input().split()))

counter = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] + A[j] <= K:
            counter += 1

print(counter)

### 6-2 ###
# 2つの整数 L,R が与えられます。
# L 以上 R 以下の整数の中から、一の位が等しくなるように相異なる 2 つの整数を選ぶ方法は何通りあるか求めるプログラムを作成してください。

L, R = map(int,input().split())

counter = 0
for i in range(L, R+1):
    for j in range(i+1, R+1):
        if i%10 == j%10:
            counter += 1

print(counter)

### 6-3 ###
# N 個の整数 A0,A1,…,AN−1が与えられます。
# 以下の条件をみたす整数の組 (x,y,z) の個数を求めるプログラムを作成してください。
# ・Ax ,Ay ,Azの最大値は Ayである。
# ・0≤x<y<z≤N−1

N = int(input())
A = list(map(int,input().split()))

counter = 0
for x in range(N):
    for y in range(x+1, N):
        for z in range(y+1, N):
            if max(A[x], A[y], A[z]) == A[y]:
                counter += 1

print(counter)

### 6-4 ###
# N 個の文字列 S0,S1,…,SN−1が与えられます。
# これらの N 個の文字列の中に同じ 2 つの文字列があるかどうかを判定するプログラムを作成してください。

N = int(input())
S = [input().split() for _ in range(N)]

flag = False
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            flag = True

if flag:
    print("Yes")
else:
    print("No")

### 6-5 ###
# 整数 N と長さ N の文字列 S が与えられます。
# 以下の条件をみたす整数の組 (x,y) の個数を数えるプログラムを作成してください。
# ・S の x 文字目と y 文字目は等しい
# ・0≤x<y≤N−1
# ただし、S の先頭の文字が 0 文字目であるとします。

N = int(input())
S = input()

counter = 0
for x in range(N):
    for y in range(x+1, N):
        if S[x] == S[y]:
            counter += 1

print(counter)
