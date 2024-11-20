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


def my_help(prio_arr, index):
    return prio_arr[index] + prio_arr[index+1]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ret_arr = [[]]*numRows
        ret_arr[0] = [1]
        ret_arr[1] = [1, 1]
        for out_i in range(2, numRows):
            x = ret_arr[out_i-1]
            for j in range(len(x)):
                print(x)

        print(ret_arr)

        # @leet end


Solution().generate(5)
