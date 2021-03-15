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

# import sys

# n = int(sys.stdin.readline())
# stack = []

# for i in range(n):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push':
#         stack.append(int(order[1]))
#     elif order[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             a = stack.pop()
#             print(a)
#     elif order[0] == 'size':
#         print(len(stack))
#     elif order[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])

# 제로

# k = int(input())
# stack = []
# for i in range(k):
#     num = int(input())
#     stack.append(num)
#     if num == 0:
#         stack.pop()
#         stack.pop()

# print(sum(stack))

# 괄호

# t = int(input())

# for i in range(t):
#     stack = []
#     chk = True
#     vps = input()
#     for i in vps:
#         if i == '(':
#             stack.append(i)
#         elif i == ')':
#             if len(stack) == 0:
#                 chk = False
#             elif stack[-1] == '(':
#                 stack.pop()
#             else:
#                 chk = False
#     if chk and len(stack) == 0:
#         print('YES')
#     else:
#         print('NO')


# 큐 2
# from collections import deque
# import sys
# n = int(sys.stdin.readline())
# queue = deque()
# for i in range(n):
#     order = sys.stdin.readline().split()

#     if order[0] == 'push':
#         queue.append(int(order[1]))
#     elif order[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             a = queue.popleft()
#             print(a)
#     elif order[0] == 'size':
#         print(len(queue))
#     elif order[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif order[0] == 'back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])

# BFS와 DFS

# from collections import deque
# graph = {}
# n, m, v = map(int, input().split())

# for i in range(n):
#     graph[i+1] = []
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x] += [y]
#     graph[y] += [x]

# start_node = v


# def dfs_stack(graph, start_node):
#     stack = [start_node]
#     visited = []
#     while stack:
#         log = stack.pop()
#         if log not in visited:
#             print(log, end=' ')
#         graph[log].sort(reverse=True)
#         visited.append(log)
#         for i in graph[log]:
#             if i not in visited:
#                 stack.append(i)


# def bfs_queue(graph, start_node):
#     queue = deque()
#     queue.append(start_node)
#     visited = []
#     while queue:
#         log = queue.popleft()
#         if log not in visited:
#             print(log, end=' ')
#         graph[log].sort()
#         visited.append(log)
#         for i in graph[log]:
#             if i not in visited:
#                 queue.append(i)


# dfs_stack(graph, start_node)
# print()
# bfs_queue(graph, start_node)

# 2108 통계학
# 시간 초과
# import math
# import sys
# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# arr.sort()
# mid = len(arr) // 2
# count_arr = []
# b = list(set(arr))
# b.sort()
# for i in b:
#     count_arr.append(arr.count(i))

# if count_arr.count(max(count_arr)) >= 2:
#     result = min(b[count_arr.index(max(count_arr))+1:])
# else:
#     result = min(b)

# print(math.round(sum(arr) / len(arr)))
# print(arr[mid])
# print(result)
# print(max(arr) - min(arr))

# 정답 코드
# import sys
# pypy3로 하면 위에 sys 안불러도 됨
# from collections import Counter
# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# arr.sort()
# mid = len(arr) // 2
# print(round(sum(arr) / len(arr)))
# print(arr[mid])

# k = Counter(arr).most_common()
# if len(arr) > 1:
#     if k[0][1] == k[1][1]:
#         print(k[1][0])
#     else:
#         print(k[0][0])
# else:
#     print(arr[0])


# print(max(arr) - min(arr))
