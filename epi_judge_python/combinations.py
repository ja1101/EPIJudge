from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    if k == 0:
        return [[]]
    if k < 0 or k > n:
        return []

    result: List[List[int]] = []
    comb = list(range(1, k + 1))
    while True:
        result.append(comb.copy())
        i = k - 1
        while i >= 0 and comb[i] == n - k + 1 + i:
            i -= 1
        if i < 0:
            break
        comb[i] += 1
        for j in range(i + 1, k):
            comb[j] = comb[j - 1] + 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
