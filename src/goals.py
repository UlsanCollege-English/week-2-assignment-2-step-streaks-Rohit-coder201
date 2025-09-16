"""Step Streaks — Solution"""

from typing import List, Tuple


def max_window_sum(values: List[int], k: int) -> Tuple[int, int] | None:
    """Return (start_index, window_sum) of the largest sum among all length-k windows.

    If k <= 0, raise ValueError. If k > len(values), return None.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    n = len(values)
    if k > n:
        return None

    window_sum = sum(values[:k])
    best_start, best_sum = 0, window_sum

    for i in range(k, n):
        window_sum += values[i] - values[i - k]
        if window_sum > best_sum:
            best_start, best_sum = i - k + 1, window_sum

    return best_start, best_sum


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    """Return how many length-k windows have average >= target_avg.

    If k <= 0, raise ValueError. If k > len(values), return 0.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    n = len(values)
    if k > n:
        return 0

    target_sum = target_avg * k
    window_sum = sum(values[:k])
    count = 1 if window_sum >= target_sum else 0

    for i in range(k, n):
        window_sum += values[i] - values[i - k]
        if window_sum >= target_sum:
            count += 1

    return count


def longest_rising_streak(values: List[int]) -> int:
    """Return the length of the longest strictly increasing consecutive streak.

    Empty list -> 0. Single element -> 1.
    """
    if not values:
        return 0

    longest = curr = 1
    for prev, nxt in zip(values, values[1:]):
        if nxt > prev:
            curr += 1
            longest = max(longest, curr)
        else:
            curr = 1
    return longest
