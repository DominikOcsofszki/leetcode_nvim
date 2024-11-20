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


class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        h = hash(key)
        print(h)
        # if key not in self.arr:
        #     self.arr.append([key, value])

    def get(self, key: int) -> int:
        pass

    def remove(self, key: int) -> None:
        pass


def test():
    # Your MyHashMap object will be instantiated and called as such:
    obj = MyHashMap()
    key = 'a'
    value = 777
    obj.put(key, value)
    print(obj)
    param_2 = obj.get(key)
    obj.remove(key)


test()
# @leet end
