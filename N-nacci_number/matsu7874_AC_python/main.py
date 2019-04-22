#!/usr/bin/env python3

MOD = 10**9+7


def solve(n, k):
    if k == 0:
        return 0

    a = [0]*(k+1)
    a[1] = 1
    a[2] = 1
    for i in range(3, n+2):
        a[i] = a[i-1]*2 % MOD
    for i in range(n+2, k+1):
        a[i] = (a[i-1]*2-a[i-n-1]) % MOD

    return a[k]


def main():
    n, m = map(int, input().split())
    print(solve(n, m))


if __name__ == "__main__":
    main()
