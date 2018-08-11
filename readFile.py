# -*- coding: utf-8 -*-

#@author: weicheng

#@file: readFile.py

#@time: 2018/08/11

def myreadline(f,newline):
    buf =''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos+len(newline):]
        chunk = f.read(4095*10)
        if not chunk:
            yield buf
            break
        buf += chunk

with open("input.txt") as f:
    for line in myreadline(f,"{/}"):
        print (line)




