# # 4949 번

# while True:
#     string = input()
#     if string == ".":
#         break
#     stack = []
#     val = True
#     for i in string:
#         if i == "(" or i == "[":
#             stack.append(i)
#         elif i == ")":
#             if len(stack) == 0:
#                 val = False
#                 break
#             if stack[-1] == "(":
#                 stack.pop()
#             else:
#                 val = False
#                 break
#         elif i == "]":
#             if len(stack) == 0:
#                 val = False
#                 break
#             if stack[-1] == '[':
#                 stack.pop()
#             else:
#                 val = False
#                 break
#     if val and not stack:
#         print('yes')
#     else:
#         print('no')

# 1874 번


# def stack_sequence(n, squence):
#     stack = []
#     count = 1
#     result = []
#     squence_index = 0
#     while True:
#         if len(stack) == 0:
#             stack.append(count)
#             result.append('+')
#             count += 1
#         elif stack[-1] == squence[squence_index]:
#             stack.pop()
#             result.append('-')
#             squence_index += 1
#             if squence_index == n:
#                 break
#         else:
#             if n < count:
#                 print('NO')
#                 break
#             stack.append(count)
#             result.append('+')
#             count += 1
#     if len(stack) == 0:
#         for i in result:
#             print(i)


# sequence = list()
# n = int(input())
# for _ in range(n):
#     sequence.append(int(input()))
# stack_sequence(n, sequence)

# 1021번
# from collections import deque
# n, m = map(int, input().split())
# number = list(map(int, input().split()))
# queue = deque()
# count = 0
# for i in range(n):
#     queue.append(i + 1)
# for i in range(len(number)):
#     if number[i] == queue[0]:
#         queue.popleft()
#         continue
#     que_index = queue.index(number[i])

#     if que_index > len(queue) // 2:
#         queue.rotate(len(queue) - que_index)
#         count += len(queue) - que_index
#     elif que_index <= len(queue) // 2:
#         queue.rotate(- que_index)
#         count += que_index
#     queue.popleft()
# print(count)
