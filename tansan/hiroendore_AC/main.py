#!/usr/bin/env python3

N, M = map(int, input().split())
a = [int(input()) for i in range(M)]
element = a[N%M]
parity = int(N/M)

if parity%2 == 1 and element == "L":
    print("T")
elif parity%2 == 1 and element == "T":
    print("L")
else:
    print(element)