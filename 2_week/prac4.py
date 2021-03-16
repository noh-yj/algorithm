# 색종이 만들기
# def square(x, y, n):
#     global paper, w_count, b_count  # 전역변수 선언
#     color = paper[y][x]
#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color != paper[j][i]:  # 범위에서 색이 같지 않다면
#                 square(x+n//2, y, n//2)  # 1사분면
#                 square(x, y, n//2)  # 2사분면
#                 square(x, y+n//2, n//2)  # 3사분면
#                 square(x+n//2, y+n//2, n//2)  # 4사분면
#                 return
#     if color == 0:
#         w_count += 1
#     else:
#         b_count += 1

# w_count = 0
# b_count = 0
# n = int(input())
# paper = []
# for i in range(n):
#     paper.append(list(map(int, input().split())))

# square(0, 0, n)
# print(w_count)
# print(b_count)


# n과 m (2)
# def dfs(cnt):
#     if cnt == M:
#         print(*arr)
#         return
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             arr.append(i+1)
#             dfs(cnt+1)
#             arr.pop()
#             for j in range(i+1, N):
#                 visited[j] = 0


# N, M = map(int, input().split())
# visited = [0 for _ in range(N)]
# arr = []
# dfs(0)

# from itertools import combinations
# N, M = map(int, input().split())
# p = combinations(range(1, N+1), M)
# for i in p:
#     print(*i)


# n-queen

# 터렛
# t = int(input())

# for i in range(t):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     r = ((x1-x2)**2 + (y1-y2)**2)**0.5
#     if r == 0 and r1 == r2:
#         print(-1)
#     elif r == r1+r2 or r2 == r1 + r or r1 == r2 + r:
#         print(1)
#     elif r > r1 + r2 or r1 > r + r2 or r2 > r + r1:
#         print(0)
#     else:
#         print(2)

# 계단 오르기
# n = int(input())
# dp = [0 for i in range(301)]
# arr = [0 for i in range(301)]
# for i in range(n):
#     arr[i] = int(input())

# dp[0] = arr[0]
# dp[1] = arr[0] + arr[1]
# dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
# for i in range(3, n):
#     dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

# print(dp[n-1])
