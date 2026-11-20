from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    def directed_combinations(offset: int,
                              partial_combination: List[int]) -> None:
        if len(partial_combination) == k:
            result.append(partial_combination.y())
            return

        num_remaining = k - len(partial_combination)
        for i in range(offset, n - num_remaining + 2):
            partial_combination.append(i)
            directed_combinations(i + 1, partial_combination)
            partial_combination.pop()

    result: List[List[int]] = []
    directed_combinations(1, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
