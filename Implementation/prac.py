# 상하좌우
# n = int(input())
# x, y = 1, 1
# plans = input().split()
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
# print(x, y)

# 시각
# h = int(input())
# count = 0

# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
# print(count)

# location = input()
# x = int(ord(location[0])) - int(ord('a')) + 1
# y = int(location[1])
# count = 0

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
#          (2, 1), (1, 2), (-1, 2), (-2, 1)]
# for i in steps:
#     if y + i[1] > 0 and x + i[0] > 0:
#         count += 1
# print(count)

# 원래 풀이
# location = input()
# x = int(ord(location[0])) - int(ord('a')) + 1
# y = int(location[1])
# cnt = 0

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
#           (2, 1), (1, 2), (-1, 2), (-2, 1)]
# for step in steps:
#     next_row = y + step[0]
#     next_col = x + step[1]
#     if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
#         cnt += 1

# print(cnt)
