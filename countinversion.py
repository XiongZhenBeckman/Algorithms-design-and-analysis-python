# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:28:51 2018

@author: Xiong Xhen
"""

#get the data
import numpy as np
data=np.loadtxt('IntegerArray.txt')
data=list(data.astype(np.int32))
def countinversion(a):    # a is a list
    if len(a)==1:
        return a,0;
    else:
        a1=a[:len(a)/2]
        a2=a[len(a)/2:len(a)]
        (a1,x)=countinversion(a1)
        (a2,y)=countinversion(a2)
        (a3,z)=countsplit(a1,a2)
        return a3,x+y+z

def countsplit(a,b):
    i=0
    j=1
    c=[]
    count=0
    new=a+b[::-1]
    for k in range(0,len(new)):
        if new[i]>new[-j]:
            c.append(new[-j])
            count=count+len(a)-i
            j=j+1
        else:
            c.append(new[i])
            i=i+1
    return c,count
