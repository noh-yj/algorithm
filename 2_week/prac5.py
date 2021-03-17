# n-queen
# import sys


# def chess(cnt):
#     global count
#     if cnt == n:
#         count += 1
#         return
#     for i in range(n):
#         if (col[i] or left[cnt+i] or right[cnt - i + n - 1]) == 0:
#             col[i] = 1
#             left[cnt+i] = 1
#             right[cnt - i + n - 1] = 1
#             chess(cnt+1)
#             col[i] = 0
#             left[cnt+i] = 0
#             right[cnt - i + n - 1] = 0


# n = int(sys.stdin.readline())
# count = 0
# col = [0]*n
# right = [0]*(2*n - 1)
# left = [0]*(2*n - 1)
# chess(0)
# print(count)

# 블랙잭
# n, m = map(int, input().split())
# card = list(map(int, input().split()))
# result = []
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             sum = card[i] + card[j] + card[k]
#             if sum <= m:
#                 result.append(sum)
# print(max(result))


# def blackjack(cnt):
#     if cnt == 3:
#         if sum(arr) <= M:
#             result.append(sum(arr))
#         return
#     for i in range(N):
#         if visited[i] == False:
#             visited[i] = True
#             arr.append(card[i])
#             blackjack(cnt+1)
#             arr.pop()
#             for j in range(i+1, N):
#                 visited[j] = False


# N, M = map(int, input().split())
# card = list(map(int, input().split()))
# visited = [False]*N
# arr = []
# result = []
# blackjack(0)
# print(max(result))

# 분해합
# n = int(input())
# k = 0
# for i in range(1, n+1):
#     k = i
#     for j in str(i):
#         k += int(j)
#     if k == n:
#         print(i)
#         break
#     if i == n:
#         print(0)

# 셀프넘버일때 처리방식 다르게하기

# n = int(input())
# k = 0
# arr = []
# for i in range(1, n+1):
#     k = i
#     for j in str(i):
#         k += int(j)
#     if k == n:
#         arr.append(i)

# if len(arr) == 0:
#     print(0)
# else:
#     print(min(arr))

# 잃어버린 괄호
# a = input().split('-')
# for i in range(len(a)):
#     if '+' in a[i]:
#         k = a[i].split('+')
#         for j in range(len(k)):
#             k[j] = int(k[j])
#         a[i] = sum(k)

# for k in range(len(a)):
#     a[k] = int(a[k])
# print(a[0] - sum(a[1:]))

# 요세푸스 문제
# from collections import deque
# n, k = map(int, input().split())
# queue = deque()
# arr = []
# for i in range(n):
#     queue.append(i+1)
# while queue:
#     queue.rotate(-k)
#     people = queue.pop()
#     arr.append(str(people))
# print('<', end='')
# print(', '.join(arr), end='')
# print('>', end='')
