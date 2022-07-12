import sys


class CircularQueue:
    def __init__(self, item):
        self.front = 0
        self.rear = 0
        self.items = [0] * item

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self, q):
        return self.front == (self.rear+1) % q

    def clear(self):
        self.front = self.rear

    def I(self, item, q):
        if not self.isFull(q):
            self.rear = (self.rear + 1) % q
            self.items[self.rear] = item
        else:
            print("overflow", end=" ")
            for i in self.items[0:q]:
                print(i, end=" ")
            print()

    def D(self, q):
        if not self.isEmpty():
            self.front = (self.front+1) % q
            tmp = self.items[self.front]
            self.items[self.front] = 0
            return tmp
        else:
            print("underflow")
            exit(0)

    def P(self, q):
        for i in self.items[0:q]:
            print(i, end=" ")
        print()


def check_num(a):
    if(a <= 0):
        print("잘못된 입력입니다...\n\n")


##### main #####
q = int(sys.stdin.readline())  # 양의 정수 q(원형 큐의 크기)
n = int(sys.stdin.readline())  # 양의 정수 n(연산의 개수)
check_num(q)
check_num(n)

c = CircularQueue(q)
c.clear()
for i in range(n):
    li = list(sys.stdin.readline().split())
    if(li[0] == 'I'):
        c.I(li[1], q)
    elif(li[0] == 'P'):
        c.P(q)
    elif(li[0] == 'D'):
        c.D(q)
    else:
        print("잘못된 입력입니다.\n프로그램을종료합니다.")
        exit(0)
