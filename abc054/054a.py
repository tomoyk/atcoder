#!/usr/bin/env python
 
# Input
Alice,Bob = [int(i) for i in input().split()]
 
if Alice==1:
  Alice = 14
 
if Bob==1:
  Bob = 14
 
if(Alice == Bob):
  print("Draw")
elif(Alice > Bob):
  print("Alice")
else:
  print("Bob")
