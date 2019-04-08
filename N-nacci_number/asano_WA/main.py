#!/usr/bin/env python3

MOD = 10**9 + 7
N,M = map(int, input().split())

def n_nacci_number(n, i):
    if i <= 0:
        return 0
    if i == 1:
        return 1
    else:
        return sum([n_nacci_number(n, i-x) for x in range(1, N+1)]) % MOD

print(n_nacci_number(N, M))