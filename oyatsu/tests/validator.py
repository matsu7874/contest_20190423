#!/usr/bin/env python3
import generator

a, b, c = map(int, input().split())
assert generator.MIN_V <= a < b < c <= generator.MAX_V, (a, b, c)
