#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
x,a,b = [int(i) for i in input().split()]
 
'''
print('x', x)
print('a', a)
print('b', b)
'''
 
if( -a+b <= 0 ):
  print('delicious')
elif( -a+b > 0 and -a+b <= x ):
  print('safe')
else:
  print('dangerous')
