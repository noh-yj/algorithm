# 2869번
# 높이, 올라가기(+), 내려가기(-) 조건: 정상으로 올라가면 미끄러지지 않는다 => break 모두 올라가는데 걸리는 날짜 count
# 시간 초과
input = input().split()
a = int(input[0])
b = int(input[1])
h = int(input[2])


def snail(a, b, h):
    count = 0
    mounting = 0
    new_mounting = 0
    while True:
        mounting = a + new_mounting
        count += 1
        new_mounting = mounting - b

        if h <= mounting:
            break
    return count


# print(snail(a, b, h))
# 수학식으로 풀이
# import sys
# import math
a, b, h = map(int, sys.stdin.readline().split())
cnt = math.ceil((h-b) / (a - b))
print(cnt)

# 10250번
# 쌓음 T = 2 , H W N 순서로 입력을 받음

a = int(input())
for i in range(a):
    hotel_num = list(map(int, input().split()))
    if hotel_num[2] % hotel_num[0] == 0:
        result = hotel_num[0]*100 + (hotel_num[2] // hotel_num[0])
    else:
        result = hotel_num[2] % hotel_num[0] * \
            100 + (hotel_num[2] // hotel_num[0] + 1)
    print(result)

# 1929번
# 소수구하기 입력: 범위값
# 함수로 풀기
a = list(map(int, input().split()))


def isPrime(input):
    if(input < 2):
        return False
    for i in range(2, int(input**0.5 + 1)):
        if(input % i == 0):
            return False
    return True


for i in range(a[0], a[1]+1):
    if(isPrime(i)):
        print(i)

# 그냥 풀기
a = list(map(int, input().split()))
check = True

for i in range(a[0], a[1]+1):
    if i == 1:
        check = False
    elif i > 1:
        check = True
    for j in range(2, int(i**0.5 + 1)):
        if(i % j == 0):
            check = False
            break
    if check:
        print(i)
