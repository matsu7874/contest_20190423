#!/usr/bin/env python3

from collections import namedtuple
import random


MIN_W = 0
MAX_W = 500
MIN_H = 0
MAX_H = 500

Case = namedtuple('Case', ('prefix', 'w', 'h'))


def main():
    num_testcase = 40
    testcases = set()

    # sample case
    testcases.add(Case('00_sample', 1, 1))
    testcases.add(Case('00_sample', 0, 2))

    # corner case
    testcases.add(Case('10_corner', MIN_W, MAX_H))
    testcases.add(Case('10_corner', MAX_W, MIN_H))
    testcases.add(Case('10_corner', MAX_W, MAX_H))

    # random case
    size_testcase = len(testcases)
    while size_testcase < num_testcase:
        w = random.randint(MIN_W, MAX_W)
        h = random.randint(MIN_H, MAX_H)
        if w == 0 and h == 0:
            continue
        if Case('20_random', w, h) not in testcases:
            testcases.add(Case('20_random', w, h))
            size_testcase += 1

    # prefixでソートして出力
    for i, (_p, w, h) in enumerate(sorted(list(testcases))):
        with open('input_{}.in'.format(i), 'w') as fout:
            fout.write('{} {}\n'.format(str(w), str(h)))


if __name__ == "__main__":
    main()
