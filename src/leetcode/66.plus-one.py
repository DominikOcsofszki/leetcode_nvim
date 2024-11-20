from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *

# @leet start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        overflow = 0
        digits[i] += 1
        if digits[i] > 9:
            overflow = 1
            digits[i] = 0
        while overflow == 1:
            overflow = 0
            i -= 1
            if i < 0:
                digits.insert(0, 1)
            else:
                digits[i] += 1
                if digits[i] > 9:
                    overflow = 1
                    digits[i] = 0

            # len_d = len(digits)
            # i = len_d-1
            # extra_1 = 0
            # while i >= 0:
            #     if digits[i] < 9:
            #         digits[i] += 1 + extra_1
            #     i -= 1

        return digits


def test_solution():
    sol = Solution()
    run = sol.plusOne
    tests = [
        [[1, 2, 3], [1, 2, 4]],
        [[4, 3, 2, 1], [4, 3, 2, 2]],
        [[9], [1, 0]],
    ]
    for test in tests:
        assert run(test[0]) == test[1], test
    print("ALL TESTS PASSED")


test_solution()
# @leet end
