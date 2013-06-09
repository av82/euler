#!/usr/bin/python -tt

import sys

def evenfibsum(k):
  a=0
  b=1
  sum=0
  evensum=0;
  while sum<k:
    print(sum )
    if sum%2==0:
       evensum=evensum+sum
    sum= a+b
    a=b
    b=sum 
  print("even sum:"+str(evensum))
def main():
 evenfibsum(int(sys.argv[1]))

main()
	

