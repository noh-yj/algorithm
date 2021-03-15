# 다리 놓기

# import math
# t = int(input())
# for i in range(t):
#     n, m = map(int, input().split())
#     result = int(math.factorial(m) / (math.factorial(m-n)*math.factorial(n)))
#     print(result)

# 동전 0

# n, k = map(int, input().split())
# coin = []
# a = []
# b = 0
# for i in range(n):
#     coin.append(int(input()))

# while True:
#     for i in coin:
#         a.append(k // i)
#     for i in range(len(a)):
#         if a[-1] == 0:
#             del a[-1]
#         elif a[-1] != 0:
#             b += min(a)
#             coin_index = a.index(min(a))
#             result = coin[coin_index]*min(a)
#             k = k - result
#             a = []
#             break
#     if k == 0:
#         break

# print(b)

# ATM

# n = int(input())
# people = list(map(int, input().split()))
# people.sort()
# a = 0
# b = []
# while True:
#     a += people[0]
#     b.append(a)
#     del people[0]
#     if len(people) == 0:
#         break

# print(sum(b))

# 스택
