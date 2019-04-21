#!/usr/bin/env python3
import generator

N, M = map(int, input().split())
a = [input() for i in range(M)]
assert generator.MIN_N <= N <= generator.MAX_N, generator.MIN_N
assert generator.MIN_M <= M <= generator.MAX_M, generator.MIN_M
