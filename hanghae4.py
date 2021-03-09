# 링크드 리스트 끝에서 K번째 값 출력하기
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         self.head = Node(value)

#     def append(self, value):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = Node(value)

#     def get_kth_node_from_last(self, k):
#         slow = self.head
#         fast = self.head

#         for i in range(k):
#             fast = fast.next
#         while fast is not None:
#             slow = slow.next
#             fast = fast.next
#         return slow


# linked_list = LinkedList(6)
# linked_list.append(7)
# linked_list.append(8)

# print(linked_list.get_kth_node_from_last(2).data)


# 주문 가능여부 판단하기
# shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
# shop_orders = ["오뎅", "콜라", "만두"]


# def is_available_to_order(menus, orders):
#     menus.sort()
#     for order in orders:
#         if not available_order(order, menus):
#             return False
#     return True


# def available_order(target, array):
#     current_min = 0
#     current_max = len(array) - 1
#     current_guess = (current_min + current_max) // 2
#     while current_min <= current_max:
#         if array[current_guess] == target:
#             return True
#         elif array[current_guess] < target:

#             current_min = current_guess + 1
#         else:
#             current_max = current_guess - 1
#         current_guess = (current_min + current_max) // 2
#     return False


# result = is_available_to_order(shop_menus, shop_orders)
# print(result)


# def is_available_to_order(menus, orders):
#     set_menus = set(menus)
#     for order in orders:
#         if order not in set_menus:
#             return False
#     return True


# result = is_available_to_order(shop_menus, shop_orders)
# print(result)
