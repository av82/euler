#!/usr/bin/python -tt

import sys
import math
  
def maxprime(num,ulimit):
   for i in range(2,ulimit): 
     if num%i==0:
       return [i] + maxprime(num/i,ulimit) 
   return[num] 
def main():
  ulimit=int(math.sqrt(long(sys.argv[1])))
  print(max(maxprime(long(sys.argv[1]),ulimit))) 
 
main()
  
