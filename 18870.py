import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
lis = list(sorted(set(li)))

dic = {lis[i]:i for i in range(len(lis))}
for i in li:
    print(dic[i], end= " ")


dic = {lis[i]:i for i in range(len(lis))}