# 바이러스
# graph = {
#     1: [2, 5],
#     2: [1, 3, 5],
#     3: [2],
#     4: [7],
#     5: [1, 2, 6],
#     6: [5],
#     7: [4]
# }

# n = int(input())
# m = int(input())
# graph = {}
# for i in range(n):
#     graph[i+1] = []
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x] += [y]
#     graph[y] += [x]


# def dfs_stack(graph, start_node):
#     stack = [start_node]
#     visited = []
#     while stack:
#         log = stack.pop()
#         visited.append(log)
#         for i in graph[log]:
#             if i not in visited:
#                 stack.append(i)

#     return visited


# a = set(dfs_stack(graph, 1))

# print(len(a) - 1)

# 피보나치
# zero_memo = [1, 0]
# one_memo = [0, 1]


# def fibo_count(n):
#     if n <= 1:
#         return
#     for i in range(2, n+1):
#         zero_memo.append(zero_memo[i-2] + zero_memo[i-1])
#         one_memo.append(one_memo[i-2] + one_memo[i-1])
#     return zero_memo, one_memo


# n = int(input())
# fibo_count(40)
# for i in range(n):
#     m = int(input())
#     print(zero_memo[m], one_memo[m])

# 11053 가장 긴 증가하는 부분 수열
# n = int(input())
# num = list(map(int, input().split()))
# dp = [1]*n
# for i in range(n):
#     for j in range(i):
#         if num[j] < num[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

# 토마토
from collections import deque

# 입력
dx = [-1, 1, 0, 0]  # 좌, 우, 상, 하
dy = [0, 0, -1, 1]
box = []
start_node = deque()
M, N = map(int, input().split())
for i in range(N):
    box.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            start_node.append([i, j])


def tomato(arr, start_node):
    queue = start_node
    while queue:
        position = queue.popleft()
        for i in range(4):
            x = position[1] + dx[i]
            y = position[0] + dy[i]

            if 0 <= x < M and 0 <= y < N and arr[y][x] == 0:
                arr[y][x] = arr[position[0]][position[1]] + 1
                queue.append([y, x])


tomato(box, start_node)

day = 0
for i in box:
    for j in i:
        if j == 0:
            day = -1
            break
        elif day < j - 1:
            day = j - 1
    if j == 0:
        break
print(day)
