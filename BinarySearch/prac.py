# 부품 찾기
# def binary(target, arr):
#     start = 0
#     end = len(arr) - 1
#     mid = start + end // 2
#     while start <= end:
#         if arr[mid] == target:
#             return print('yes', end=' ')
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#         mid = (start + end) // 2
#     return print('no', end=' ')


# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# m = int(input())
# target_arr = list(map(int, input().split()))

# for i in target_arr:
#     result = binary(i, arr)

# 떡볶이 떡 만들기
n, m = map(int, input().split())
target_arr = list(map(int, input().split()))

start = 0
end = max(target_arr)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in target_arr:
        if mid <= i:
            total += i - mid
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
