class Node:
    """
    링크드 리스트의 노드 클래스
    """
    def __init__(self, data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def delete_after(self, previous_node):
        """링크드 리스트 삭제연산. 주어진 노드 뒤 노드를 삭제한다"""
        data = previous_node.next.data

        # 지우려는 노드가 tail 노드일 때
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        # 두 노드 사이 노드를 지울 때
        else:
            previous_node.next = previous_node.next.next

        # 링크드 리스트에서 노드를 삭제할 때는 지워지는 노드의 데이터를 리턴하는 것이 관습이다
        return data

    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        data = self.head.data

        # 삭제 하려는 데이터가 링크드 리스트의 마지막 남은 데이터일 때
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return data

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:  # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:  # 링크드 리스트가 비어 있는 경우
            # 새로운 노드가 링크드 리스트의 처음이자 마지막 노드가 된다
            self.head = new_node
            self.tail = new_node
        else:  # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드 추가
            self.tail = new_node  # 마지막 노드를 추가한 노드로 변경

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        iterator = self.head

        # 링크드 리스트를 끝까지 돈다
        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# # 데이터 2, 3, 5, 7, 11을 담는 노드들 생성
# head_node = Node(2)
# node_1 = Node(3)
# node_2 = Node(5)
# node_3 = Node(7)
# tail_node = Node(11)
#
# # 노드들을 연결
# head_node.next = node_1
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = tail_node
#
# # 노드 순서대로 출력
# iterator = head_node
#
# while iterator is not None:
#     print(iterator.data)
#     iterator = iterator.next

# --------------------------------------------

# 새로운 링크드 리스트 생성
# my_list = LinkedList()
#
# # 링크드 리스트에 데이터 추가
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.append(11)
#
# # iterator = my_list.head
# #
# # while iterator is not None:
# #     print(iterator.data)
# #     iterator = iterator.next
#
# print(my_list)

# --------------------------

# # 접근연산
# # 새로운 링크드 리스트 생성
# my_list = LinkedList()
#
# # 링크드 리스트에 데이터 추가
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.append(11)
#
# # 링크드 리스트 노드에 접근 (데이터 가지고 오기)
# print(my_list.find_node_at(3).data)
#
# # 링크드 리스트 노드에 접근 (데이터 바꾸기)
# my_list.find_node_at(2).data = 13
#
# print(my_list)

# -------------------------

# # 탐색연산
# # 새로운 링크드 리스트 생성
# linked_list = LinkedList()
#
# # 여러 데이터를 링크드 리스트 마지막에 추가
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(5)
# linked_list.append(7)
# linked_list.append(11)
#
# # 데이터 2를 갖는 노드 탐색
# node_with_2 = linked_list.find_node_with_data(2)
#
# if not node_with_2 is None:
#     print(node_with_2.data)
# else:
#     print("2를 갖는 노드는 없습니다")
#
# # 데이터 11을 갖는 노드 탐색
# node_with_11 = linked_list.find_node_with_data(11)
#
# if not node_with_11 is None:
#     print(node_with_11.data)
# else:
#     print("11를 갖는 노드는 없습니다")
#
# # 데이터 6 갖는 노드 탐색
# node_with_6 = linked_list.find_node_with_data(6)
#
# if not node_with_6 is None:
#     print(node_with_6.data)
# else:
#     print("6을 갖는 노드는 없습니다")

# -------------------------------

# # 삽입 연산
# # 새로운 링크드 리스트 생성
# my_list = LinkedList()
#
# # 링크드 리스트에 데이터 추가
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
#
# print(my_list)
#
# node_2 = my_list.find_node_at(2)  # 인덱스 2에 있는 노드 접근
# my_list.insert_after(node_2, 6)  # 인덱스 2뒤에 6삽입
#
# print(my_list)
#
# head_node = my_list.head  # 헤드 노드 접근
# my_list.insert_after(head_node, 9)  # 헤드 노드 뒤에 9삽입
#
# print(my_list)

# # 가장 앞에 데이터 삽입
#
# # 새로운 링크드 리스트 생성
# linked_list = LinkedList()
#
# # 여러 데이터를 링크드 리스트 앞에 추가
# linked_list.prepend(11)
# linked_list.prepend(7)
# linked_list.prepend(5)
# linked_list.prepend(3)
# linked_list.prepend(2)
#
# print(linked_list)  # 링크드 리스트 출력
#
# # head, tail 노드가 제대로 설정됐는지 확인
# print(linked_list.head.data)
# print(linked_list.tail.data)

# ------------------------------------
# 링크드 리스트 삭제

# # 새로운 링크드 리스트 생성
# my_list = LinkedList()
#
# # 링크드 리스트에 데이터 추가
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.append(11)
#
# print(my_list)
#
# node_2 = my_list.find_node_at(2)  # 인덱스2 노드 접근
# my_list.delete_after(node_2)  # 인덱스2 뒤 데이터 삭제
#
# print(my_list)
#
# second_to_last_node = my_list.find_node_at(2)  # 맨 끝에서 두 번째 노드 접근
# print(my_list.delete_after(node_2))  # tail 노드 삭제;
#
# print(my_list)

# 링크드 리스트 가장 앞 삭제
# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.prepend(11)
linked_list.prepend(9)
linked_list.prepend(5)
linked_list.prepend(3)
linked_list.prepend(2)

print(linked_list)  # 링크드 리스트 출력

# 가장 앞 노드 계속 삭제
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())

print(linked_list)  # 링크드 리스트 출력
print(linked_list.head)
print(linked_list.tail)
