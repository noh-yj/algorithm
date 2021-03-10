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
