# 위에서 아래로

a = int(input())
arr = []
for i in range(a):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')
