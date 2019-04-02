#!/usr/bin/env python3

a, b, c = map(int, input().split())
print(min(a*b+c, a+b*c))
