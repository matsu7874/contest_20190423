#!/usr/bin/env python3
# 貪欲法

N,M = map(int, input().split())
a = []
for i in range(M):
    a.append(int(input()))

a = sorted(a)
a.reverse()

rest = N
for x in a:
    rest -= (N // x) * x

if rest == 0:
	print("Yes")
else:
	print("No")