import sys
import math

N, K = map(int, sys.stdin.readline().split())

N2 = math.factorial(N)
N_K = math.factorial(N-K)
K2 = math.factorial(K)

print(int(N2/(N_K*K2)))