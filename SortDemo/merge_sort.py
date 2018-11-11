#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

def merge_sort(a:List[int]):
    _merge_sort_between(a,0,len(a)-1)

def _merge_sort_between(a:List[int],low:int,high:int):
    if low >= high:
        return
    mid = low + (high-low) //2
    print (mid)
    _merge_sort_between(a, low, mid)
    _merge_sort_between(a, mid + 1, high)
    _merge(a,low,mid,high)




def _merge(a:List[int],low:int,mid:int,high:int):
    i,j = low,mid+1
    tmp = []
    while i <=mid and j<=high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end  = mid if i<= mid else high
    tmp.extend(a[start:end+1])
    print(tmp)
    a[low:high+1] = tmp


if __name__ == "__main__":
    a1 = [3,5,8,7,6]
    merge_sort(a1)
