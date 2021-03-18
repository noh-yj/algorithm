# 1만들기
# n = int(input())
# dp = [0]*(n+1)

# for i in range(1, n+1):
#     if i == 1:
#         dp[i] = 0
#         continue
#     dp[i] = dp[i-1] + 1
#     if i % 3 == 0 and dp[i//3]+1 < dp[i]:
#         dp[i] = dp[i//3] + 1
#     elif i % 2 == 0 and dp[i//2] + 1 < dp[i]:
#         dp[i] = dp[i//2] + 1
# print(dp[n])

# N = int(input())
# wine = [0]
# maxi = [0]*(N+1)
# for i in range(1, N+1):
#     wine.append(int(input()))
#     if i < 3:
#         maxi[i] = sum(wine)
#     else:
#         target = []
#         target.append(maxi[i-3]+wine[i-1]+wine[i])
#         target.append(maxi[i-2]+wine[i])
#         target.append(maxi[i-1])
#         maxi[i] = max(target)
# print(maxi[-1])
