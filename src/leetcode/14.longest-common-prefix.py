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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_string = min(strs, key=len)
        for word_i in range(len(strs)):
            for letter_i in range(len(strs)):

        return min_string

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        min_string = min(strs, key=len)
        for i, item in enumerate(min_string):
            for word in strs:
                if word[i] != item:
                    return word[0:i]
        return min_string
        # @leet end


res = Solution().longestCommonPrefix(["flower", "flow", "flight"])
res2 = Solution().longestCommonPrefix(["dlower", "flow", "flight"])

print(res)
print(res2)
