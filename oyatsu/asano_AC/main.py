#!/usr/bin/env python3

N,M = map(int, input().split())
a = []
for i in range(M):
    a.append(int(input()))

dp = [i == 0 for i in range(N+1)]

for m in range(1, M+1):
    price = a[m-1]
    for n in range(price, N+1):
        if not dp[n]:
            dp[n] = dp[n-price]

if dp[N]:
    print("Yes")
else:
    print("No")