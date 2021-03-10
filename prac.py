
n = int(input())
num = list(map(int, input().split()))
length = [1]*n

for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            length[i] = max(length[i], length[j] + 1)

print(max(length))
