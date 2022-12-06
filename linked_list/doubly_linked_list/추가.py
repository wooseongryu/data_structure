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

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        iterator = self.head

        # 링크드 리스트를 끝까지 돈다
        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 빈 링크드 리스트 정의
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)
