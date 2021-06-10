# dfs: 깊이 우선 탐색으로 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# stack에 방문처리를 담음
# 재귀적 풀이
# def dfs(graph, start, visited):
#     visited[start] = True
#     print(start, end=' ')
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# graph = [[], [2, 8, 3], [1, 7], [1, 4, 5],
#          [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
# visited = [False]*9
# dfs(graph, 1, visited)
