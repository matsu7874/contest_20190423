#!/usr/bin/env python3
import generator

N, M = map(int, input().split())
assert generator.MIN_N <= N <= generator.MAX_N and generator.MIN_M <= M <= generator.MAX_M, (N, M)
