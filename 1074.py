import sys

N, r, c = map(int, sys.stdin.readline().split())

print("Input test", end=" ")
print(N, r, c)

ans = 0

# 3 7 7

while N != 0:
    N -= 1  # N = 2 r,c ==7, N = 1
    print("N:", N)
    # 1사분면
    if(r < 2**N and c >= 2**N):
        ans += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)

    # 2사분면
    elif(r < 2**N and c < 2**N):
        ans += (2 ** N) * (2 ** N) * 0

    # 3사분면
    elif(r >= 2**N and c < 2**N):
        ans += (2 ** N) * (2 ** N) * 2
        r -= 2**N

    # 4사분면
    elif(r >= 2**N and c >= 2**N):
        ans += (2**N) * (2**N) * 3
        c -= 2**N  # N = 2
        r -= 2**N  # r,c = 3, 7-4 =3,
        # r,c = 1,1

    # 에러 처리
    else:
        print("ERR:: algorithm err...")
    print("r : ", r)
    print("c :", c)
    print("ans :", ans)

print(ans)
