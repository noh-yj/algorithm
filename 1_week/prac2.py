# 4344번

# test case 는 반의 갯수
# 평균을 넘는(초과) 학생의 비율을 구하자, 소숫점 셋째자리까지 출력

a = int(input())
for i in range(a):
    number = list(map(int, input().split()))
    b = []
    score = number[1:]
    student = number[0]
    average = sum(score) / student
    for i in score:
        if i > average:
            b.append(i)
    result = len(b) / student
    print(format(result, '.3%'))


# 4673번
# !self_number = d(n) (n과 각 자리수를 더함) ex) 75 75 + 7 + 5 >> a_num = n + n//10 + n%10
# 조건 n > 0 (양의 정수)
# 접근: 전체에서 - !self_num


def self_num():
    all_num = set(range(1, 10001))
    num = set()
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        num.add(i)
    result = sorted(all_num - num)
    for i in result:
        print(i)


self_num()


# 1157번
# 가장 많이 사용된 알파벳 구하기, 조건: 대, 소문자 구분하지 않음, 주어진 단어의 길이는 최대 백만
# 일단 다 대문자로 만들기(o), 중복값 조회, 많이 사용된 알파벳이 2개 이상이면 ? 로 출력
# Mississipi zZa

word = str(input()).upper()
set_word = list(set(word))
count_word = []

for i in set_word:
    count_word.append(word.count(i))
if count_word.count(max(count_word)) >= 2:
    print('?')
else:
    max_index = count_word.index(max(count_word))
    print(set_word[max_index])


# 2941번
word = input().replace('c=', '1').replace('c-', '1').replace('dz=', '1').replace('d-',
                                                                                 '1').replace('lj', '1').replace('nj', '1').replace('s=', '1').replace('z=', '1').split()
cnt = len(word[0])
print(cnt)
