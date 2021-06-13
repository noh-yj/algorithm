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

# 게임 개발
# n, m = map(int, input().split())
# # m*n 공간 생성
# d = [[0]*m for _ in range(n)]
# # direction = 0: 북 1: 동 2: 남 3: 서
# x, y, direction = map(int, input().split())

# d[x][y] = 1  # 시작 좌표
# # 현재 지형 정보 추가
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))

# # 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 왼쪽으로 회전


# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3


# count = 1
# turn_time = 0
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]

#     if d[nx][ny] == 0 and arr[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1

#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]

#         if arr[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0

# print(count)
