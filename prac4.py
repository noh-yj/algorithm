# 배열 내 최대값 구하기
a = [3, 5, 6, 1, 2, 4]

# 방법 1
print(max(a))
# 방법 2
max_num = a[0]
for i in a:
    if max_num < i:
        max_num = i

print(max_num)

# 최빈값 찾기
input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    find_arr = [0]*26
    for char in string:
        if not char.isalpha():
            continue

        find_alpha = ord(char) - ord('a')
        find_arr[find_alpha] += 1
    max_alpha = 0
    max_alpha_index = 0
    for i in range(len(find_arr)):
        if find_arr[i] > max_alpha:
            max_alpha = find_arr[i]
            max_alpha_index = i
    return chr(max_alpha_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)

# 배열에서 특정 요소 찾기
input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for i in array:
        if i == number:
            return True
    return False


result = is_number_exist(3, input)
print(result)

# 조건 N >= 0, 배열 내 합, 곱을 했을때 최고값 출력하기
input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    a = 0
    for i in array:
        if i <= 1 or a <= 1:
            a += i
        else:
            a *= i
    return a


result = find_max_plus_or_multiply(input)
print(result)

# 반복되지 않는 문자
input = "abadabac"


def find_not_repeating_first_character(string):
    alpha_arr = [0]*26
    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        alpha_arr[index] += 1
    not_repeat_arr = []
    for i in range(len(alpha_arr)):
        if(alpha_arr[i] == 1):
            not_repeat_arr.append(chr(i + ord('a')))

    for char in string:
        if char in not_repeat_arr:
            return char


result = find_not_repeating_first_character(input)
print(result)

# 소수 나열하기
input = 20


def find_prime_list_under_number(number):
    a = []
    chk = True
    for i in range(2, number + 1):
        chk = True
        for j in range(2, int(i**0.5 + 1)):
            if i % j == 0:
                chk = False
                break
        if chk:
            a.append(i)
    return a


result = find_prime_list_under_number(input)
print(result)

# 문자열 요약하기


def summarize_string(input_str):
    n = len(input_str)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if input_str[i] == input_str[i + 1]:
            count += 1
        else:
            result_str += input_str[i] + str(count + 1) + '/'
            count = 0

    result_str += input_str[n - 1] + str(count + 1)

    return result_str


input_str = "acccdeee"

print(summarize_string(input_str))

# 문자열 뒤집기 모두 000 또는 111 로 만들어주면 됨
# 첫번째 숫자를 기준으로 접근, 인접숫자로 접근
input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    all_one = 0
    all_zero = 0
    if string[0] == '0':
        all_one += 1
    elif string[0] == '1':
        all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i + 1] == "1":
                all_zero += 1
            if string[i + 1] == '0':
                all_one += 1

    return min(all_one, all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
