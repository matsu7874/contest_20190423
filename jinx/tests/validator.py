#!/usr/bin/env python3
import generator

w, h = map(int, input().split())
assert generator.MIN_W <= w <= generator.MAX_W, w
assert generator.MIN_W <= h <= generator.MAX_W, h
assert w > 0 or h > 0, (w, h)
