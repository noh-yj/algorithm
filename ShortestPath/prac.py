# 최단 경로
# 가장 짧은 경로를 찾는 알고리즘, 길찾기 문제

# 다익스트라 최단 경로 알고리즘: 그래프에서 여러개의 노드가 있을 때 특청 노드에서 출발해서 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
# 음의 간선이 없을때 정상적으로 작동

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# # 노드 개수, 간선 개수
# n, m = map(int, input().split())
# # 시작 노드
# start = int(input())

# graph = [[] for i in range(n+1)]

# visited = [False] * (n+1)
# distanse = [INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))


# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n+1):
#         if distanse[i] < min_value and not visited[i]:
#             min_value = distanse[i]
#             index = i
#     return index


# def dijkstra(start):
#     distanse[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distanse[j[0]] = j[1]

#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True

#         for j in graph[now]:
#             cost = distanse[now] + j[1]

#             if cost < distanse[j[0]]:
#                 distanse[j[0]] = cost


# dijkstra(start)

# for i in range(1, n+1):
#     if distanse[i] == INF:
#         print('INFINITY')
#     else:
#         print(distanse[i])


# 힘 자료 구조 사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
