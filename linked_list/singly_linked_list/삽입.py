class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

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

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

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


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

node_2 = my_list.find_node_at(2)  # 인덱스 2에 있는 노드 접근
my_list.insert_after(node_2, 6)  # 인덱스 2뒤에 6삽입

print(my_list)

head_node = my_list.head  # 헤드 노드 접근
my_list.insert_after(head_node, 9)  # 헤드 노드 뒤에 9삽입

print(my_list)
