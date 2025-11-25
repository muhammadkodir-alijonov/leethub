# k is always positive. 
# find length of the smallest integer n (length).
# n is divisible by k.
# n only contains the digit 1: main point.
# if there is no n, we can just return -1.

# note: 111... is not diviisble by even number that 2,4,6,7,so we must ignore even number. 

# we can use hashtable, list and other collections but the most faster one is hashtable 

# last we can make a number only 111...11.1.1.1
# logic: just multiply 10 and +1
"""
Ex 1:
    k = 1 
    ans: 1
Ex 2:
    k = 2
    ans: -1
Ex 3:
    k = 3
    ans = 111
"""
from typing import List
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # n is always start with 1
        n = 1
        # base case
        if k % 2 == 0 or k % 5 == 0:
            return -1
        # main point
        len = 1
        while True:
            if n % k == 0:
                return len
            len += 1
            n = n*10 +1 # a new number only contains 1