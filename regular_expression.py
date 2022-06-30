#### 正規表現 ####

####メタ文字 その 1 ####

### 1-1 ###
# 文字列 S が与えられます。
# 文字列 S が algo という文字列を含むか判定するプログラムを作成してください。

import re

S = input()
reg = "algo"

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")


### 1-2 ###
# 文字列 S が与えられます。
# 文字列 S が以下の形式を満たすか判定するプログラムを作成してください。
# meth{o, 1つ以上}d


import re

S = input()
reg = r'^metho+d$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

### 1-3 ###
# 文字列 S が与えられます。
# 文字列 S が以下の形式を満たすか判定するプログラムを作成してください。
# a{1個以上5個以下}  b{10個}c{0個以上}

import re

S = input()
reg = r'^a{1,5}b{10}c*$'

search = re.search(reg, S)
if search:
  print("Yes")
else:
  print("No")


### 1-4 ###
# 文字列 S が与えられます。
# 文字列 S が cat または dog という文字列を含むか判定するプログラムを作成してください。

import re

S = input()
reg = r'cat|dog'

search = re.search(reg, S)
if search:
  print("Yes")
else:
  print("No")


#### エスケープ文字 ####

### 2-1 ###
# 文字列 S が与えられます。
# 文字列 S が 1+1 という文字列を含むか判定するプログラムを作成してください。

import re

S = input()
reg = r'1\+1'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")


### 2-2 ###
# 文字列 S が与えられます。
# 文字列 S に括弧書きが含まれるか判定するプログラムを作成してください。
# ただし、括弧書きは「 ( と ) で挟まれた 1 文字以上の文字列 」のこととします。

import re

S = input()
reg = r'\(.+\)'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")


### 2-3 ###
# 文字列 S が与えられます。
# 文字列 S が 英文として成立しているか判定するプログラムを作成してください。
# ただし、以下の条件をみたすとき「英文として成立している」とします。
# 「S0-S1 -. . .- SN」という形式で表される。
# ただし、Si  は 1 文字以上の英小文字列とする。(0 ≤ i ≤ N)

import re

S = input()
reg = r'^([a-z]+\-)*[a-z]+$'

search = re.search(reg, S)
if search:
  print("Yes")
else:
  print("No")


#### メタ文字 その 2 ####

### 3-1 ###
# 文字列 S が与えられます。
# 文字列 S が数字を含むか判定するプログラムを作成してください。

import re

S = input()
reg = r'\d'

search = re.search(reg,S)
if search:
    print("Yes")
else:
    print("No")

### 3-2 ###
# 文字列 S が与えられます。
# 文字列 S が位置が連続する 3 文字以上の数字を含むか判定するプログラムを作成してください。

import re

S = input()
reg = r'\d{3,}'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

### 3-3 ###
# 文字列 S が与えられます。
# 文字列 S が以下の形式を満たすか判定するプログラムを作成してください。
# (数字が 3 つ) - (数字が 4 つ)

import re

S = input()
reg = r'^\d{3}\-\d{4}$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

### 3-4 ###
# 文字列 S が与えられます。
# 文字列 S が以下の形式を満たすか判定するプログラムを作成してください。
# (1文字以上の半角英数字) @ (1 文字以上の半角英数字) . (1文字以上 4 文字以下の半角英数字)

import re

S = input()
reg = r'^[0-9a-zA-Z]+\@[0-9a-zA-Z]+\.[0-9a-zA-Z]{1,4}$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")


#### 先読み・後読み ####

### 4-1 ###
# 英小文字のみからなる文字列 S が与えられます。
# 文字列 S のうち、r に挟まれた(両隣の文字が r である) u を a に置換するプログラムを作成してください。

import re
S = input()

print(re.sub(r'ru(?=r)', 'ra', S))

# ↑解説
# rur を rarに置換する方法だと、最初に rur をマッチした時点で、右側の r がその次の rur にマッチすべき r を読んでしまう
# それを回避するために、肯定先読みを使う。つまり、ru(?=r) を ra に置換すればよい。ここで先読みされた (?=r) はマッチした部分とはみなされず、u と r の間にマッチする。

### 4-2 ###
# 空白区切りの複数単語からなる英文字列 S が与えられます。
# 文字列 S の中にある asian という単語のあとに 5 単語以上が続くならば、その asian を global に置き換えた文字列を出力してください。

import re
S = input()

print(re.sub(r'asian(?=( [a-z]+){5,})', 'global', S))

### 4-3 ###
# 英小文字のみからなる文字列 S が与えられます。
# 文字列 S のなかに、algo のあとに来るのが rithm でも method でもないような、algo + 5 文字以上の文字からなる部分文字列が含まれているかを答えてください。

import re
S = input()

search = re.search(algo(?!method)(?!rithm)[a-z]{5,})
if search:
    print("Yes")
else:
    print("No")
