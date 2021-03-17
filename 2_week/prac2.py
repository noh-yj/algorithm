# 신나는 함수 실행
# dp = [[[0 for i in range(101)] for j in range(101)] for k in range(101)]


# def w(a, b, c):
#     if dp[a][b][c] != 0:
#         return dp[a][b][c]
#     if a <= 0 or b <= 0 or c <= 0:
#         dp[a][b][c] = 1
#         return dp[a][b][c]
#     elif a > 20 or b > 20 or c > 20:
#         dp[a][b][c] = w(20, 20, 20)
#         return dp[a][b][c]
#     elif a < b and b < c:
#         dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#         return dp[a][b][c]
#     else:
#         dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
#             w(a-1, b, c-1) - w(a-1, b-1, c-1)
#         return dp[a][b][c]


# while True:
#     a, b, c = map(int, input().split())
#     if a == -1 and b == -1 and c == -1:
#         break
#     print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))

# 파도반 수열
# dp = {
#     1: 1,
#     2: 1,
#     3: 1
# }


# def triangle(n, dp):
#     if n in dp:
#         return dp[n]
#     nth_triangle = triangle(n-2, dp) + triangle(n-3, dp)
#     dp[n] = nth_triangle
#     return nth_triangle


# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(triangle(n, dp))

# RGB 거리

# n = int(input())
# rgb_list = []
# for i in range(n):
#     rgb = list(map(int, input().split()))
#     rgb_list.append(rgb)

# dp = []
# dp.append(rgb_list[0])

# for i in range(1, n):
#     temp = []
#     temp.append(min(dp[i-1][1], dp[i-1][2]) + rgb_list[i][0])  # r
#     temp.append(min(dp[i-1][0], dp[i-1][2]) + rgb_list[i][1])  # g
#     temp.append(min(dp[i-1][0], dp[i-1][1]) + rgb_list[i][2])  # b
#     dp.append(temp)
# print(min(dp[n-1]))

# 정수 삼각형
# n = int(input())
# sum_arr = []
# for i in range(n):
#     num = list(map(int, input().split()))
#     sum_arr.append(num)

# for i in range(1, n):
#     for j in range(i + 1):
#         if j == 0:
#             sum_arr[i][j] = sum_arr[i][j] + sum_arr[i-1][j]
#         elif i == j:
#             sum_arr[i][j] = sum_arr[i][j] + sum_arr[i-1][j-1]
#         else:
#             sum_arr[i][j] = max(
#                 (sum_arr[i][j] + sum_arr[i-1][j-1]), (sum_arr[i][j] + sum_arr[i-1][j]))
# print(max(sum_arr[n-1]))
# 제일 왼쪽은 제일 왼쪽 위에꺼 위치 더해주고 오른쪽도 동일
# 가운데 애들은 위에 숫자중에 가장 큰거만 뽑아주면 됨

# 약수

# n = int(input())
# num = list(map(int, input().split()))

# if n % 2 == 0:
#     num.sort()
#     print(num[0]*num[-1])
# elif n % 2 != 0:
#     num.sort()
#     mid = len(num)//2
#     print(num[mid]**2)
# 방법 2
# print(max(num)*min(num))

# 최대공약수와 최소공배수

# num = list(map(int, input().split()))
# num.sort()
# x, y = num[1], num[0]

# while y != 0:
#     x = x % y
#     x, y = y, x
# print(x)
# print(num[0]*num[1] // x)

# 최소공배수
# n = int(input())
# for i in range(n):
#     num = list(map(int, input().split()))
#     num.sort()
#     x, y = num[1], num[0]
#     while y != 0:
#         x = x % y
#         x, y = y, x
#     print(num[0]*num[1]//x)

# 이항 계수
# import math
# n, k = map(int, input().split())
# if k < 0 or k > n:
#     print(0)
# else:
#     print(int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k))))
