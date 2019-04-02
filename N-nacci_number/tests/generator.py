#!/usr/bin/env python3

from collections import namedtuple
import random


MIN_V = 0
MAX_V = 100

Case = namedtuple('Case', ('prefix', 'a', 'b', 'c'))


def main():
    num_testcase = 40
    testcases = set()

    # sample case
    testcases.add(Case('00_sample', 3, 5, 7))
    testcases.add(Case('00_sample', 98, 99, 100))

    # corner case
    testcases.add(Case('10_corner', 0, 1, 100))

    # random case
    size_testcase = len(testcases)
    while size_testcase < num_testcase:
        a = random.randint(MIN_V, MAX_V-2)
        b = random.randint(a+1, MAX_V-1)
        c = random.randint(b+1, MAX_V)
        if Case('20_random', a, b, c) not in testcases:
            testcases.add(Case('20_random', a, b, c))
            size_testcase += 1

    # prefixでソートして出力
    for i, (_p, a, b, c) in enumerate(sorted(list(testcases))):
        with open('input_{}.in'.format(i), 'w') as fout:
            fout.write('{} {} {}\n'.format(str(a), str(b), str(c)))


if __name__ == "__main__":
    main()
