# 11729번


# def hanoitop(n, start, end):
#     if n == 1:
#         print(start, end)
#         return

#     hanoitop(n-1, start, 6-start-end)  # hanoi(n-1)
#     print(start, end)  # 큰 원판 이동
#     hanoitop(n-1, 6-start-end, end)  # hanoi(n-1)


# n = int(input())
# print(2**n - 1)
# hanoitop(n, 1, 3)


# 2805번
# N, M = map(int, input().split())
# tree_length = list(map(int, input().split()))
# current_min = 1
# current_max = max(tree_length)

# while current_min <= current_max:
#     current_mid = (current_min + current_max) // 2
#     want_length = 0
#     for i in tree_length:
#         if current_mid <= i:
#             want_length += i - current_mid

#     if want_length >= M:
#         current_min = current_mid + 1
#     else:
#         current_max = current_mid - 1

# print(current_max)
