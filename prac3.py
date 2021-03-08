# 2869번
# 높이, 올라가기(+), 내려가기(-) 조건: 정상으로 올라가면 미끄러지지 않는다 => break 모두 올라가는데 걸리는 날짜 count

# input = input().split()
# a = int(input[0])
# b = int(input[1])
# h = int(input[2])

# def snail(a, b, h):
#     count = 0
#     mounting = 0
#     new_mounting = 0
#     while True:
#         mounting = a + new_mounting
#         count += 1
#         new_mounting = mounting - b

#         if h <= mounting:
#             break
#     return count


# print(snail(a, b, h))

# import math
# import sys
# a, b, h = map(int, sys.stdin.readline().split())
# cnt = math.ceil((h-b) / (a - b))
# print(cnt)

# 10250번
# 쌓음 T = 2 , H W N 순서로 입력을 받음

# a = int(input())
# for i in range(a):
#     hotel_num = list(map(int, input().split()))
#     if hotel_num[2] % hotel_num[0] == 0:
#         result = hotel_num[0]*100 + (hotel_num[2] // hotel_num[0])
#     else:
#         result = hotel_num[2] % hotel_num[0] * \
#             100 + (hotel_num[2] // hotel_num[0] + 1)
#     print(result)

# 1929번
# 소수구하기 입력: 범위값

# a = list(map(int, input().split()))

# num = set(range(a[0], a[1]+1))
# new_num = set()

# for i in range(a[0], a[1]+1):
#     for j in range(1, 1000001):
#         if i // j == 1:
#             new_num.add(j)


# print(new_num)
