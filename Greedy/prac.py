# 거스름돈 문제

# n = 1260
# count = 0

# coin_type = [500, 100, 50, 10]
# for i in coin_type:
#     a = n // i
#     count += a
#     n %= i
# print(count)


# 큰 수의 법칙
# n, m, k = map(int, input().split())
# number = list(map(int, input().split()))
# number.sort()
# first = number[-1]
# second = number[-2]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
# print(result)

# 숫자 카드 게임
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     card = list(map(int, input().split()))
#     min_value = min(card)
#     result = max(result, min_value)

# print(result)

# 1이 될 때까지
# n, k = map(int, input().split())
# count = 0
# while True:
#     if n % k == 0:
#         if n == 1:
#             break
#         n = n // k
#         count += 1
#     else:
#         if n == 1:
#             break
#         n = n - 1
#         count += 1
# print(count)
