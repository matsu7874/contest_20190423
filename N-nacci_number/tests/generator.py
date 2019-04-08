#!/usr/bin/env python3

from collections import namedtuple
import random


MIN_N, MAX_N = 2, 100
MIN_M, MAX_M = 0, 5 * 10**5

Case = namedtuple('Case', ('prefix', 'N', 'M'))


def main():
    num_testcase = 40
    testcases = set()

    # sample case
    testcases.add(Case('00_sample', 2, 5))
    testcases.add(Case('00_sample', 4, 6))
    testcases.add(Case('00_sample', 100, 0))

    # large case
    testcases.add(Case('10_large', 100, 5 * 10**5))

    # random case
    size_testcase = len(testcases)
    while size_testcase < num_testcase:
        N = random.randint(MIN_N, MAX_N)
        M = random.randint(MIN_M, MAX_M)
        if Case('20_random', N, M) not in testcases:
            testcases.add(Case('20_random', N, M))
            size_testcase += 1

    for i, (_p, N, M) in enumerate(sorted(list(testcases))):
        with open('input_{}.in'.format(i), 'w') as fout:
            fout.write('{} {}\n'.format(str(N), str(M)))


if __name__ == "__main__":
    main()
