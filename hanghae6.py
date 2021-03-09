# 스택
# 기능: push(data): 맨 앞에 데이터 넣기(append), pop() 맨 앞의 데이터 뽑기, peek() 맨 앞 데이터 조회, isEmpty(): 스택 비었는지 여부 판단

# top_heights = [6, 9, 5, 7, 4]


# def get_receiver_top_orders(heights):
#     answer = [0]*len(heights)
#     while heights:
#         height = heights.pop()
#         for i in range(len(heights) - 1, -1, -1):
#             if heights[i] > height:
#                 answer[len(heights)] = i + 1
#                 print(answer)
#                 break
#     return answer


# print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

# 큐
# 기능: enqueue(data) : 맨 뒤에 데이터 추가하기 dequeue() : 맨 앞의 데이터 뽑기 peek() : 맨 앞의 데이터 보기 isEmpty(): 큐가 비었는지 안 비었는지 여부 반환해주기
# from collections import deque
# queue = deque([4, 5, 6])
# queue.append(7)
# queue.append(8)
# print(queue)
# queue.popleft()
# print(queue)
# 해쉬 사용 > 배열의 길이로 나눈 나머지 값을 사용, put(key, value): key에 value 저장, get(key): key에 해당하는 value 가져오기
# hash("fast") % len(arr)
# all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
# present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# def get_absent_student(all_array, present_array):
#     dict = {}
#     for key in all_array:
#         dict[key] = True  # 아무 값이나 넣어도 상관 없습니다! 여기서는 키가 중요한거니까요

#     for key in present_array:  # dict에서 key 를 하나씩 없앱니다
#         del dict[key]

#     for key in dict.keys():  # key 중에 하나를 바로 반환합니다! 한 명 밖에 없으니 이렇게 해도 괜찮습니다.
#         return key


# print(get_absent_student(all_students, present_students))
