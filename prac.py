# stack queue 1, 2, 3
# while True:
#     string = input()
#     stack = []
#     answer = True
#     if string == ".":
#         break

#     for i in string:
#         if i == '(' or i == '[':
#             stack.append(i)

#         elif i == ')':
#             if len(stack) == 0:
#                 answer = False
#                 break
#             elif stack[-1] == '(':
#                 stack.pop()
#             else:
#                 answer = False
#                 break
#         elif i == ']':
#             if len(stack) == 0:
#                 answer = False
#                 break
#             elif stack[-1] == '[':
#                 stack.pop()
#             else:
#                 answer = False
#                 break
#     if answer and len(stack) == 0:
#         print('yes')
#     else:
#         print('no')


# def stack_arr(n, arr):
#     stack = []
#     result = []
#     count = 1
#     index = 0
#     while True:
#         if len(stack) == 0:
#             stack.append(count)
#             result.append('+')
#             count += 1
#         elif stack[-1] == arr[index]:
#             stack.pop()
#             result.append('-')
#             index += 1
#             if index == n:
#                 break
#         else:
#             if count > n:
#                 print('NO')
#                 break
#             stack.append(count)
#             result.append('+')
#             count += 1
#     if len(stack) == 0:
#         for i in result:
#             print(i)


# n = int(input())
# arr = list()
# for i in range(n):
#     arr.append(int(input()))
# stack_arr(n, arr)

# from collections import deque

# n, m = map(int, input().split())
# number = list(map(int, input().split()))
# queue = deque()
# for i in range(n):
#     queue.append(i + 1)
# count = 0
# for i in range(len(number)):
#     if queue[0] == number[i]:
#         queue.popleft()
#         continue
#     que_index = queue.index(number[i])

#     if que_index > len(queue) // 2:
#         queue.rotate(len(queue) - que_index)
#         count += len(queue) - que_index
#     elif que_index < len(queue) // 2:
#         queue.rotate(-que_index)
#         count += que_index
# print(count)

# hanoi

# def hanoi_top(n, start, end):
#     if n == 1:
#         print(start, end)
#         return
#     hanoi_top(n-1, start, 6-start-end)
#     print(start, end)
#     hanoi_top(n-1, 6-start-end, end)


# n = int(input())
# print(2**n - 1)
# hanoi_top(n, 1, 3)

# 좌표 정렬
# n = int(input())
# arr = list()
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#     arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
# arr.sort()
# for i in range(len(arr)):
#     print(arr[i][1], arr[i][0])

# 나무 자르기, 이분탐색
# n, m = map(int, input().split())
# tree = list(map(int, input().split()))
# current_min = 1
# current_max = max(tree)
# while current_min <= current_max:
#     current_guess = (current_min + current_max) // 2
#     tree_length = 0

#     for i in tree:
#         if i >= current_guess:
#             tree_length += i - current_guess

#     if tree_length >= m:
#         current_min = current_guess + 1
#     else:
#         current_max = current_guess - 1
# print(current_max)
