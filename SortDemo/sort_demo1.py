#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List



def bubble_sort(a:List[int]) -> List[int]:
    if len(a) <= 1:
        return a

    for i in range(len(a)):
        made_swap = False
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                made_swap = True
        if not made_swap:
            break
    return a

def insertion_sort(a:List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    for i in range(1,len(a)):
        value = a[i]
        j = i - 1
        while j>=0 and a[j] > value:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value
    return a


def selection_sort(a:List[int]) -> List[int]:

    if len(a) <= 1:
        return a
    for i in range(len(a)):
        min_index = i
        min_val = a[i]
        for j in range(i,len(a)):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]








