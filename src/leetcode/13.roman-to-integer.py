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
    def romanToInt(self, s: str) -> int:
        print("s:", s)
        ctd = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'],
                   [1, 5, 10, 50, 100, 500, 1000]))

        hashm: dict = dict(
            IV=4, IX=9,
            XL=40, XC=90,
            CD=400, CM=900,
            # *ctd
        )
        hashm.update(ctd)
        es = 0
        check = set(['I', 'X', 'C'])
        rem = ''
        for index, item in enumerate(s):
            print("==============ITEM: ", item)
            if rem and hashm.get(rem+item, None):
                es += hashm.get(rem+item)
            elif rem:
                es += hashm.get(rem)
                # es += hashm.get(item)

            if item in check:
                print("in check:", item)
                rem = item
            else:
                es += hashm.get(item)
                rem = ''
            if index == len(s)-1 and rem:
                es += hashm.get(rem)
            print(es)
        print(es)
        return es


def test_solution():
    tests = [
        ["III", 3],
        ["LVIII", 58],
        ["MCMXCIV", 1993],
    ]
    sol = Solution()
    run = sol.romanToInt
    for test in tests:
        assert run(test[0]) == test[1], test


test_solution()
# @leet end
