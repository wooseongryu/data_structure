class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def insert_after(self, previous_node, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 마지막 노드 뒤에 삽입할 때
        if previous_node is self.tail:
            self.tail.next = new_node  # 새 노드를 tail노드의 다음으로 지정
            new_node.prev = self.tail  # tail노드를 새 노드의 전 노드로 지정
            self.tail = new_node  # 새 노드를 tail노드로 지정
        # 두 노드 사이에 삽입할 때
        else:
            # 새 노드를 기존의 링크드 리스트에 연결
            new_node.prev = previous_node
            new_node.next = previous_node.next

            # 기존의 노드들의 앞과 다음 레퍼런스를 새롭게 생성한 노드로 지정
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)  # 새로운 데이터를 저장하는 노드

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # 링크드 리스트에 데이터가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

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

# 새로운 노드 5개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

# tail 노드 뒤에 노드 삽입
tail_node = my_list.tail  # 4 번째(마지막)노드를 찾는다
my_list.insert_after(tail_node, 5)  # 4 번째(마지막)노드 뒤에 노드 추가
print(my_list)
print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
my_list.insert_after(node_at_index_2, 2)
print(my_list)
