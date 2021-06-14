# 정렬: 데이터를 특정한 기준에 따라서 순서대로 나열

# 선택 정렬: 가장 작은 것을 선택한다는 의미에서 선택 정렬 알고리즘이라 함, 알고리즘 문제 풀이에 사용하기에는 느린편
# arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(arr)):
#     min_idx = i
#     for j in range(i+1, len(arr)):
#         if arr[min_idx] > arr[j]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]

# print(arr)

# 삽입 정렬: 특정한 데이터를 적절한 위치에 삽입하는 알고리즘
# arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):
#         if arr[j] < arr[j - 1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#         else:
#             break
# print(arr)
