#!/usr/bin/env python3

n, m = map(int, input().split())
p = [int(input()) for _ in range(m)]

dp = [False] * (n+1)
dp[0] = True

for i in range(m):
    for j in range(p[i], n + 1):
        if not dp[j] and dp[j-p[i]]:
            dp[j] = True

print('Yes' if dp[n] else 'No')
