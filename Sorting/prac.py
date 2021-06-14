# 위에서 아래로
# a = int(input())
# arr = []
# for i in range(a):
#     arr.append(int(input()))

# arr.sort(reverse=True)

# for i in arr:
#     print(i, end=' ')

# 성적이 낮은 순서로 학생 출력하기
# a = int(input())
# arr = []


# def setting(data):
#     return int(data[1])


# for i in range(a):
#     arr.append(input().split())
# result = sorted(arr, key=setting)
# for i in result:
#     print(i[0], end=' ')

# 두 배열의 원소 교체
# n, k = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# arr1.sort()
# arr2.sort(reverse=True)

# for i in range(k):
#     if arr1[i] < arr2[i]:
#         arr1[i], arr2[i] = arr2[i], arr1[i]
#     else:
#         break
# print(sum(arr1))
