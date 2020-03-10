'''
入力は以下の形式で標準入力から与えられる。
S (S : 文字列)
s = input()

入力は以下の形式で標準入力から与えられる。
n (n : 整数)
n = int(input())

入力は以下の形式で標準入力から与えられる。
n (n : 小数)
n = float(input())

入力は以下の形式で標準入力から与えられる。
S_1 S_2 (S_1, S_2 : 文字列)
ex1.
s = input().split()
ex2.
s_1, s_2 = map(str, input().split())

入力は以下の形式で標準入力から与えられる。
A B (A, B : 整数)
a, b = map(int, input().split())

入力は以下の形式で標準入力から与えられる。
a_1 a_2 ⋯ a_N (a_i : 整数)
ex1.
a = list(map(int, input().split()))
ex2.
a = [int(x) for x in input().split()]

入力は以下の形式で標準入力から与えられる。
a_1
a_2_
⋮
a_N
ex1.
a = []
for _ in range(N):
    a.append(input())
ex2.
a = [input() for _ in range(N)]

入力は以下の形式で標準入力から与えられる。
x_1 y_1 z_1
x_2 y_2 z_2
⋮⋮
x_N y_N z_N
x = [0] * N
y = [0] * N
z = [0] * N
for i in range(N):
    x[i], y[i], z[i] = map(int, input().split())

'''



