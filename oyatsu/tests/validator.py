#!/usr/bin/env python3
import generator

N,M = map(int, input().split())
a = []
for i in range(M):
	a.append(int(input()))

assert generator.MIN_N <= N <= generator.MAX_N
assert generator.MIN_M <= M <= generator.MAX_M
assert len([i for i in a if i < generator.MIN_a or i > generator.MAX_a]) == 0