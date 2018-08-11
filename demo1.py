# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo1.py

#@time: 2018/08/11

from collections.abc import Iterator


class Company(object):

    def __init__(self,employ_list):
        self.employee = employ_list


    def __iter__(self):
        return MyIterator(self.employee)

    #def __getitem__(self, item):
        #return self.employee[item]

class MyIterator(Iterator):

    def __init__(self,employ_list):
        self.iter_list = employ_list
        self.index = 0



    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word




if __name__ == "__main__":
    company = Company(["a","b","c"])
    my_itor = iter(company)
    while True:
        try:
            print (next(my_itor))
        except StopIteration:
            pass

