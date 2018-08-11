# -*- coding: utf-8 -*-

#@author: weicheng

#@file: how_to_work.py

#@time: 2018/08/11


"""
python 一切都是对象
"""
import inspect
import dis

def gen_func():
    yield 1
    name = "lele"
    yield 2
    age = 30
    return "immoc"
gen = gen_func()

print (dis.dis(gen))

print (gen.gi_frame.f_lasti)
print (gen.gi_frame.f_locals)














