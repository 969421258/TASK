#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    try:
        fh.write("this is a che shi weng jian!!")
    finally:
        print "clouse the tesk"
        fh.close()
except IOError:
    print "Error: no zao dao weng jian or weng jian cuo wu"
