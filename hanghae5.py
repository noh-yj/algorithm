# 버블 정렬
# input = [4, 6, 2, 9, 1]


# def bubble_sort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]


# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
# 선택 정렬
# input = [4, 6, 2, 9, 1]


# def selection_sort(array):
#     for i in range(len(array) - 1):
#         min_index = i
#         for j in range(len(array) - i):
#             if array[i+j] < array[min_index]:
#                 min_index = i + j
#         array[i], array[min_index] = array[min_index], array[i]


# selection_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

# 삽입 정렬
# input = [4, 6, 2, 9, 1]


# def insertion_sort(array):
#     for i in range(1, len(array)):
#         for j in range(i):
#             if array[i-j-1] > array[i-j]:
#                 array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
#             else:
#                 break


# insertion_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

# 병합 정렬
# array_a = [1, 2, 3, 5]
# array_b = [4, 6, 7, 8]


# def merge(array1, array2):
#     result = []
#     array1_index = 0
#     array2_index = 0
#     while array1_index < len(array1) and array2_index < len(array2):
#         if array1[array1_index] < array2[array2_index]:
#             result.append(array1[array1_index])
#             array1_index += 1
#         else:
#             result.append(array2[array2_index])
#             array2_index += 1
#     if array1_index == len(array1):
#         while array2_index < len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#     if array2_index == len(array2):
#         while array2_index < len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#     return result


# print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
# array = [5, 3, 2, 1, 6, 8, 7, 4]


# array = [5, 3, 2, 1, 6, 8, 7, 4]


# def merge_sort(array):
#     if len(array) <= 1:
#         return array
#     mid = len(array) // 2
#     left_array = array[:mid]
#     right_array = array[mid:]
#     return merge(merge_sort(left_array), merge_sort(right_array))
