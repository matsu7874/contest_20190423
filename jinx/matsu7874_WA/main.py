#!/usr/bin/env python3

w, h = map(int, input().split())
mod = 10**9+7
dp = [[[0]*(h+4) for j in range(w+4)] for i in range(2)]
dp[0][1][1] = 1
for i in range(1, w+3):
    for j in range(1, h+3):
        dp[0][i+1][j] += dp[0][i][j]
        dp[0][i][j+1] += dp[0][i][j]
        dp[1][i-1][j] += dp[0][i][j]
        dp[1][i][j-1] += dp[0][i][j]
for i in range(w+2):
    for j in range(h+2):
        dp[1][i+1][j] += dp[1][i][j]
        dp[1][i][j+1] += dp[1][i][j]
print(dp[1][w+1][h+1] % mod)