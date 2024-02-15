# 第4版 ラムダ関数の利用
from collections import Counter


def get_number_with_highest_count(counts):
    return max(
        counts,
        key=lambda number: counts[number]
    )


def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)


print(most_frequent([0, 3, 5, 10, 20, 5, 3, 4, 20, 4, 5, 3, 12, 4]))
