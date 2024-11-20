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
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val < list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

    #     lr = ListNode()
    #     start = lr
    #     l1 = list1
    #     l2 = list2
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
    #     while l1 or l2:
    #         print(l1, l2)
    #         if not l1:
    #             lr.next = l2
    #             return start.next
    #         if not l2:
    #             lr.next = l1
    #             return start.next
    #         if l1.val <= l2.val:
    #             lr.next = l2
    #             l2 = l2.next
    #         else:
    #             lr.next = l1
    #             l1 = l1.next
    #         lr = lr.next
    #
    #     return start.next


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1 and not list2:
#             return None
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         l1_pointer = list1
#         l2_pointer = list2
#         lret = ListNode()
#         start = lret
#         print("list1 "+str(list1))
#         print("list2 "+str(list2))
#
#         while l1_pointer or l2_pointer:
#             print(l1_pointer, l2_pointer)
#             if not l1_pointer:
#                 lret.next = l2_pointer
#                 return start.next
#             if not l2_pointer:
#                 lret.next = l1_pointer
#                 return start.next
#
#             print(l1_pointer.val > l2_pointer.val)
#             if l1_pointer.val >= l2_pointer.val:
#                 lret.next = l1_pointer
#                 l1_pointer = l1_pointer.next
#             else:
#                 lret.next = l2_pointer
#                 l2_pointer = l2_pointer.next
#             lret.next = lret.next.next
#
#         return start
#

# @leet stop
