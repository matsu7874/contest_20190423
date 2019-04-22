#!/usr/bin/env python3

from collections import namedtuple
import random
import time

MIN_M = 1
MAX_M = 100

MIN_N = 1
MAX_N = 100000

MIN_a = 1
MAX_a = 100000

class TestCase:
    def __init__(self, N, M, a):
        self.N = N
        self.M = M
        self.a = a

    def equals(self, case):
        if self.N != case.N:
            return False
        if self.M != case.M:
            return False
        for i in self.a:
            if not i in case.a:
                return False
        return True

def make_dplist(M, a):
    N = MAX_N
    dp = [i == 0 for i in range(N+1)]
    for m in range(1, M+1):
        price = a[m-1]
        for n in range(price, N+1):
            if not dp[n]:
                dp[n] = dp[n-price]
    return dp

def main():
    num_testcase = 40
    testcases = []

    # sample case
    testcases.append(TestCase(100, 3, [80, 30, 40]))
    testcases.append(TestCase(100, 4, [60, 90, 80, 15]))

    # corner case
    testcases.append(TestCase(100, 3, [101, 209, 329]))
    testcases.append(TestCase(MAX_N, MAX_M, [MAX_N-2-i for i in range(MAX_M-1)] + [MAX_M//2 + 1]))
    testcases.append(TestCase(MAX_N, MAX_M, [MIN_a]*MAX_M))
    testcases.append(TestCase(MAX_N, MAX_M, [MIN_a+i for i in range(MAX_M)]))

    # worst case on DP
    testcases.append(TestCase(MAX_N, MAX_M, [1 for i in range(MAX_M)]))

    # simple case
    size_testcase = len(testcases)
    while size_testcase < num_testcase - 20:
        M = random.randint(MIN_M, MAX_M // 5)
        a = random.sample(range(MIN_a, MAX_a // 10 + 1), M)
        answer = make_dplist(M, a)
        max_no = max([i for i in range(MAX_N + 1) if not answer[i]])
        candidate = None
        if max_no >= 100:
            if max_no == MAX_N:
                candidate = TestCase(random.randint(MAX_a//10, MAX_N), M, a)
            elif random.randint(0,1) == 0:
                # No
                candidate = TestCase(max_no, M, a)
            else:
                # Yes
                candidate = TestCase(random.randint(max_no + 1, MAX_N), M, a)

            for case in testcases:
                if candidate.equals(case):
                    continue

            testcases.append(candidate)
            size_testcase += 1

    # complex case
    while size_testcase < num_testcase:
        M = random.randint(MAX_M // 5, MAX_M) if size_testcase < num_testcase - 10 else MAX_M
        a = random.sample(range(MAX_a // 10000, MAX_a + 1), M)
        answer = make_dplist(M, a)
        max_no = max([i for i in range(MAX_N + 1) if not answer[i]])
        if max_no >= 40000:
            if max_no == MAX_N:
                candidate = TestCase(random.randint(MAX_N // 2, MAX_N), M, a)
            elif random.randint(0,1) == 0:
                # No
                candidate = TestCase(max_no, M, a)
            else:
                # Yes
                candidate = TestCase(random.randint(max_no + 1, MAX_N), M, a)

            for case in testcases:
                if candidate.equals(case):
                    continue

            testcases.append(candidate)
            size_testcase += 1
    # prefixでソートして出力
    for i, case in enumerate(testcases):
        with open('input_{}.in'.format(i), 'w') as fout:
            fout.write('{} {}\n'.format(str(case.N), str(case.M)))
            for i in range(case.M):
                fout.write('{}\n'.format(str(case.a[i])))

if __name__ == "__main__":
    main()
