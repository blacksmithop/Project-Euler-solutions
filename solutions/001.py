"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from typing import Tuple, List


upper = 1000

def is_mult(n: int, nums: List[int]) -> Tuple[bool, int]:
    for i in nums:
        if n % i == 0:
            return True, n
    return False, 0

sum_n : int = 0

for i in range(1, upper):
    flag, res = is_mult(i, [3,5])
    if flag:
        sum_n += res

print(f"Sum of multiples", sum_n)
