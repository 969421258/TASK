Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
#!/usr/bin/python
#-*- coding: UTF-8 -*-


class Student:
    stu_count = 0
    def __init__(self,stu_no,name,stu_class,male):
        self.stu_no = stu_no
        self.name = name
        self.stu_class = stu_class
        self.male = male
        Student.stu_count += 1
        
    def displayCountByClass(self):
        print"total student %d" % Student.stu_count
        
    def displaystu(self):
        print "Name :",self.name, ",student number :",self.stu.no ",stu_class :",self.stu_class ",male :",self.male
