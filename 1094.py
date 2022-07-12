import sys
'''
https://www.acmicpc.net/problem/1094
'''
'''
# 사용할 자료형 = 리스트 :: 추가, 삭제, len연산 등이 쉽기 때문에
# =============================================================
import sys


def main():
    init_num = 64
    li = [init_num]  # [64]

    pro_num = int(sys.stdin.readline())  # int(input())

    if(pro_num > 64):
        print("ERR:: input number err...")
        return 0
    else:
        while(sum(li) != pro_num):
            li.sort()  # [4,16] [2,2,16]
            div_num = li.pop(0) // 2
            if(div_num != 0):
                li.append(div_num)
                li.append(div_num)
            li.sort()
            print(li)

            if(len(li) != 1):
                print("h1")
                if(sum(li[1:]) >= pro_num):
                    continue
            else:
                print("h2")
                if(sum(li) >= pro_num):
                    continue

    print(len(li))
    return 0


if __name__ == "__main__":
    main()
'''

# =============================================================

'''
64
-
32 32
-
32 16 16
-
32 16 8 8
32 16 8
-
32 16 4 4
32 16 4
-
32 16 2 2
32 16 2
-
32 16 1 1
32 16 1
-
32 16
-
32 8 8
.
.
.

1 2 4 16 = 23
'''


def main():
    pro_num = int(sys.stdin.readline())
    pro_num_str = str(format(pro_num, 'b'))
    print(pro_num_str)
    return print(pro_num_str.count("1"))


if __name__ == "__main__":
    main()
