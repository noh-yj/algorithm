# n과 m

# def nandm(cnt):
#     if cnt == m:
#         print(*arr)
#         return
#     for i in range(n):
#         if visited[i] == 0:
#             visited[i] = 1
#             arr.append(i+1)
#             nandm(cnt+1)
#             visited[i] = 0
#             arr.pop()


# n, m = map(int, input().split())
# visited = [0]*n
# arr = []
# nandm(0)

# 수 찾기
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# m = int(input())
# target = list(map(int, input().split()))

# for i in target:
#     min_arr = 0
#     max_arr = len(arr) - 1
#     while min_arr <= max_arr:
#         mid_arr = (min_arr + max_arr) // 2
#         if arr[mid_arr] == i:
#             print(1)
#             break
#         elif arr[mid_arr] < i:
#             min_arr = mid_arr + 1
#         else:
#             max_arr = mid_arr - 1
#     else:
#         print(0)

# 01 타일
# n = int(input())
# dp = [0]*1000001
# dp[1] = 1
# dp[2] = 2

# for i in range(3, n+1):
#     dp[i] = (dp[i-1] + dp[i-2]) % 15746

# print(dp[n])
