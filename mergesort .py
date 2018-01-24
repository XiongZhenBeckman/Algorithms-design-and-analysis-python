# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:52:03 2018

@author: zhen xiong
"""


def merge(a,b):   # a,b are list
    i=0;
    j=1;
    c=[];
    new=a+b[::-1]
    for k in range(0,len(new)):
        if new[i]<new[-j]:
            c.append(new[i])
            i=i+1
        else:
            c.append(new[-j])
            j=j+1
    return c
            
def mergesort(a):    # a is a list
    a1=a[:len(a)/2]
    a2=a[len(a)/2:len(a)]
    if len(a)>2:
        a1=mergesort(a1)
        a2=mergesort(a2)
    return merge(a1,a2);
            