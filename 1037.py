import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

if(len(li) == 1):
    print(li[0] * li[0])
else:
    print(min(li)* max(li))