#!/usr/bin/env python3
# 枝刈りのある全探索

N,M = map(int, input().split())
a = []
for i in range(M):
    a.append(int(input()))

a = sorted(a)

def canPayExactly(n, i):
    if n == 0:
        return True
    if i >= M:
        return False

    price = a[i]
    if n < price:
        return False

    for x in range(n // price + 1):
        if canPayExactly(n - price*x, i+1):
            return True
    return False

if canPayExactly(N, 0):
    print("Yes")
else:
    print("No")