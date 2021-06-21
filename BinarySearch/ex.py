# 이진탐색 / 변수를 3개 사용 시작, 끝점, 중간점
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는것
# 재귀를 사용하는 방법이 있고, 단순 반복문을 이용하는 방식이 있다.

# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = start + end // 2
#         # 중간 인덱스
#         if arr[mid] == target:
#             return mid
#             # 타겟을 찾으면 중간값 반환
#         elif arr[mid] > target:
#             end = mid - 1
#             # 중간점보다 타겟이 작으면 왼쪽 확인
#         else:
#             start = mid + 1
#             # 중간점보다 타겟이 크면 오른쪽 확인
#     return None


# n, target = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# result = binary_search(arr, target, 0, n-1)
# if result == None:
#     print('no')
# else:
#     print(result + 1)

# ex
# finding_target = 14
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# def is_existing_target_number_binary(target, array):
#     current_min = 0
#     current_max = len(array) - 1
#     current_guess = (current_min + current_max) // 2

#     while current_min <= current_max:
#         if array[current_guess] == target:
#             return True
#         elif array[current_guess] < target:
#             current_min = current_guess + 1
#         else:
#             current_max = current_guess - 1
#         current_guess = (current_max + current_min) // 2

#     return False


# result = is_existing_target_number_binary(finding_target, finding_numbers)
# print(result)
