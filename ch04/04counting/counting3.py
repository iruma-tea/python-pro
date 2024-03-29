# 第3版 Counterの利用
from collections import Counter


def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)


print(most_frequent([0, 3, 5, 10, 20, 5, 3, 4, 20, 4, 5, 3, 12, 4]))
