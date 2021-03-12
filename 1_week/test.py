# 수 정렬하기


# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# arr.sort()

# for i in arr:
#     print(i)

# 카드 2
# from collections import deque
# n = int(input())
# queue = deque()
# for i in range(n):
#     queue.append(i+1)

# while len(queue) > 1:
#     queue.popleft()
#     queue.rotate(-1)

# print(queue[0])

# 숫자 카드 이분탐색

# n = int(input())
# arr_n = list(map(int, input().split()))
# arr_n.sort()
# m = int(input())
# arr_m = list(map(int, input().split()))
# a = []
# for i in arr_m:
#     min_num = 0
#     max_num = n - 1
#     result = 0
#     while min_num <= max_num:
#         mid_num = (min_num + max_num) // 2
#         if i == arr_n[mid_num]:
#             result = 1
#             break
#         elif i > arr_n[mid_num]:
#             min_num = mid_num + 1
#         else:
#             max_num = mid_num - 1
#     a.append(str(result))

# print(' '.join(a))
