# 2588번
a, b = map(int, input().split())

print(a * ((b) % 10))
print(a * ((b//10) % 10))
print(a * (b//100))
print(a*b)


# 2884번

a, b = map(int, input().split())

if b >= 45:
    print(a, b - 45)
elif a > 0 and b < 45:
    print(a - 1, b + 15)
else:
    print(a + 23, b + 15)


# 1110번
# 26이면 2 + 6 = 8 = > 68

# first_num % 10 은 6 first_num // 10 은 2
# second_num = ((first_num % 10)*10) + (first_num // 10 + first_num % 10)

num = int(input())

check_num = num
new = 0
a = 0
count = 0

while True:
    a = num // 10 + num % 10
    new = (num % 10)*10 + a % 10
    count += 1
    num = new

    if new == check_num:
        break

print(count)
