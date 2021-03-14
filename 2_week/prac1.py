# 그룹단어 체크
# n = int(input())
# count = 0
# for i in range(n):
#     word = input()
#     for i in range(len(word)):
#         if i != len(word) - 1:
#             if word[i] == word[i + 1]:
#                 pass
#             elif word[i] in word[i + 1:]:
#                 break
#         else:
#             count += 1


# print(count)

# 설탕 배달
# n = int(input())
# b = []
# for i in range(n):
#     for j in range(n):
#         if n == 5*i + 3*j:
#             b.append(i+j)
# if len(b):
#     print(min(b))
# else:
#     print(-1)

# n = int(input())
# count = 0
# while n >= 0:
#     if n % 5 == 0:
#         count += n // 5
#         print(count)
#         break
#     n = n - 3
#     count += 1
# else:
#     print(-1)

# fly me to the alpha centauri

# t = int(input())
# for i in range(t):
#     x, y = map(int, input().split())
#     diff = y - x

#     if diff <= 3:
#         print(diff)
#     else:
#         n = int(diff**0.5)
#         if diff == n**2:
#             print(2*n - 1)
#         elif n**2 < diff <= n**2 + n:
#             print(2*n)
#         else:
#             print(2*n + 1)


# 베르트랑 공준
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     answer = True
#     count = 0
#     for i in range(n + 1, 2*n + 1):
#         if i == 1:
#             answer = False
#         elif i > 1:
#             answer = True
#         for j in range(2, int(i**0.5 + 1)):
#             if i % j == 0:
#                 answer = False
#                 break
#         if answer:
#             count += 1
#     print(count)

# 영화감독 숌
# n = int(input())
# num = 666

# while n:
#     if '666' in str(num):
#         n -= 1
#     num += 1
# print(num - 1)
