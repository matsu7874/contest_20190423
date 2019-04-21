#!/usr/bin/env python3

from collections import namedtuple
import random


MIN_N = 1
MAX_N = 1000000000

MIN_M = 1
MAX_M = 100000

MIN_a = 1
MAX_a = 100000

class TestCase:
    def __init__(self, _p, N, M, a):
        self._p = _p
        self.N = N
        self.M = M
        self.a = a


def main():
    num_testcase = 40
    testcases = []

    # sample case
    testcases.append(TestCase('00_sample', 5, 3, ["L", "T", "T"]))
    testcases.append(TestCase('00_sample', 100, 5, ["T", "L", "T", "L", "T"]))

    # corner case
    #testcases.add(Case('10_corner', 0, 1, 100))

    # random case
    size_testcase = len(testcases)
    while size_testcase < num_testcase:
        N = random.randint(MIN_N, MAX_N)
        M = random.randint(MIN_M, MAX_M)
        a = random.choices(["T", "L"], k=M)
        if TestCase('20_random', N, M, a) not in testcases:
            testcases.append(TestCase('20_random', N, M, a))
            size_testcase += 1

    # prefixでソートして出力
    for i, case in enumerate(testcases):
        with open('input_{}.in'.format(i), 'w') as fout:
            fout.write('{} {}\n'.format(str(case.N), str(case.M)))
            for i in range(case.M):
                fout.write('{}\n'.format(str(case.a[i])))


if __name__ == "__main__":
    main()
