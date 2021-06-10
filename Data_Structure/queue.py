# queue 선입선출 구조, 예) 놀이공원 줄서기
# from collections import deque 사용
from collections import deque

queue = deque()
# append, popleft() 사용

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 자료형으로 변경 시 list()를 활용
print(list(queue))
queue.reverse()
print(list(queue))
