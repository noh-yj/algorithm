# 스테인 알고리즘

# a, b = map(int, input().split())


# def gcd(a, b):
#     cnt = 0
#     num = 0
#     while ((a | b) & 1 == 0):
#         cnt += 1
#         a >>= 1
#         b >>= 1
#     while(a != 0 and b != 0):
#         while((a & 1) == 0):
#             a >>= 1
#         while((b & 1) == 0):
#             b >>= 1
#         if (a > b):
#             a = a-b
#         else:
#             b = b-a
#     if (a != 0):
#         num = a
#     else:
#         num = b
#     return num << cnt


# print(gcd(a, b))


# 1차원 오름차순에서 최단거리 구하기
# a = int(input())
# list = list(map(int, input().split()))
# b = []

# for i in range(a-1):
#     b.append(list[i+1] - list[i])

# print(min(b))

# [템플릿] UI Event
n, m = map(int, input().split())
arr = [[0]*1000 for _ in range(1000)]
button_cnt = [0]*(n+1)

for i in range(n):
    btn = list(map(int, input().split()))
    for j in range(btn[0], btn[1]+1):
        for k in range(btn[2], btn[3] + 1):
            arr[j][k] = i+1

for j in range(m):
    x, y = map(int, input().split())
    button_cnt[arr[x][y]] += 1

for i in range(n):
    print('Button #%d:' % int(i+1), button_cnt[i+1])
