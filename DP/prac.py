# 1로 만들기

# x = int(input())
# d = [0]*30001

# for i in range(2, x+1):
#     d[i] = d[i-1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5] + 1)
# print(d[x])

# 개미 전사

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0] * 100

# dp[0] = arr[0]
# dp[1] = max(arr[0], arr[1])

# for i in range(2, n):
#     dp[i] = max(arr[i-1], arr[i-2]) + arr[i]

# print(dp[n-1])

# 바닥 공사
# n = int(input())
# dp = [0] * 1001

# dp[1] = 1
# dp[2] = 3
# for i in range(3, n + 1):
#     dp[i] = (dp[i-1] + dp[i-2]*2) % 796796

# print(dp[n])

# 효율적인 화폐 구성

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# dp = [10001] * (m+1)

# dp[0] = 0
# for i in range(n):
#     for j in range(arr[i], m+1):
#         if dp[j - arr[i]] != 10001:
#             dp[j] = min(dp[j], dp[j - arr[i]] + 1)

# if dp[m] == 10001:
#     print(-1)
# else:
#     print(dp[m])
