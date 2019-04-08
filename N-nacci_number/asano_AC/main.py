#!/usr/bin/env python3
MOD = 10**9 + 7
N,M = map(int, input().split())
if M == 0:
    print(0)
    exit()
a = [0 for i in range(M+1)]
a[1] = 1

for i in range(2,M+1):
    left = i - N
    if left < 0:
        left = 0
    a[i] = sum(a[left:i]) % MOD

print(a[M])
