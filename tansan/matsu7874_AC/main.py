#!/usr/bin/env python3

n,m = map(int, input().split())
n -= 1
a = [input() for i in range(m)]

if n // m % 2 == 0:
    print(a[n%m])
else:
    print('T' if a[n%m]=='L' else 'L')
