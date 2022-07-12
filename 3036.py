import sys
import math

N = int(input())

li = list(map(int, sys.stdin.readline().split()))

reu = []
red = []

for i in range(1,N):
    g = math.gcd(li[0],li[i])
    reu.append(li[0]//g)
    red.append(li[i]//g)

for i in range(N-1):
    print(reu[i],end="")
    print("/",end="")
    print(red[i],end="")
    print()
