finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)


def count_down(number):
    if number < 0:
        return
    print(number)
    count_down(number - 1)


count_down(60)


def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)


print(factorial(5))

input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i - 1]:
            return False
    return True


print(is_palindrome(input))

input = "abcba"


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))
