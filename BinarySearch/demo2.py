#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List


def bsearch_leff(nums:List[int],target:int) -> int:
    low,high = 0,len(nums)-1
    while low <= high:
        mid = low +(high-low)//2
        if nums[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return low if nums[low] == target else -1


def bsearch_right(nums:List[int],target:int) -> int:
    low,high = 0 ,len(nums) -1
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] <= target:
            low = mid +1
        else:
            high = mid -1
    return high if nums[high] == target else -1


def bsearch_left_not_less(nums:List[int],target:int) -> int:
    low,high = 0 ,len(nums) -1
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] < target:
            low = mid +1
        else:
            high = mid-1
    return low if low < len(nums) else -1


def bsearch_right_not_greater(nums:List[int],target:int) -> int:

    low,high = 0 ,len(nums) -1
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return high if high >0 else -1


