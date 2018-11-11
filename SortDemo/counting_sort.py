#!/usr/bin/env python
# -*- coding:utf-8 -*-


from typing import List
import itertools

def counting_sort(a:List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    counts = [0]*(max(a)+1)
    for num in a:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))
    a_sorted = [0] * len(a)
    for num in reversed(a):
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1
    return a_sorted

