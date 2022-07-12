#addr : 19986
# page num : 4
#offset : 3602

# print(19986/20)


# 19986 = x * 4 +3602

# print(19986-3602)
# print(16384/4096) # 4096 = 2^12

#bit = int(input("bits : "))
#page = int(input("page size : "))
#page2 = page * 8000
#i = 1
#cnt = 0
# while(True):
#    sum = i**2
#    cnt += 1
#    if(sum == page2):
#        break
# print(cnt)
#x = int(input())
#x2 = x // 2**12
#x3 = x % (2**12)
#print(x2, x3)
s = "70120304230321201701"


def opt(size, pages):
    Size = size
    memory = []
    faults = 0
    for page in pages:
        if(memory.count(page) == 0 and len(memory) < Size):
            memory.append(page)
            faults += 1
        elif(memory.count(page) == 0 and len(memory) == Size):
            memory.pop(0)
            memory.append(page)
            faults += 1
        elif(memory.count(page) > 0):
            memory.remove(page)
            memory.append(page)
    return faults


print(opt(32, s))
