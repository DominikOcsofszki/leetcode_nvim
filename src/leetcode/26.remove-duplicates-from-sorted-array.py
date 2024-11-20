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
    def removeDuplicates(self, nums: List[int]) -> int:
        check = {}
        lst = []
        for i, item in enumerate(nums):
            if item not in check:
                check[item] = item
                lst.append(i)

        unique = len(lst)
        for i, i_item in enumerate(lst):
            nums[i] = nums[i_item]
        return unique


# input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# # print(input)
# x = Solution().removeDuplicates(input)
# # print(input)
#
# print(x)
# @leet end
