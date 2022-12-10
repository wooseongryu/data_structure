from collections import deque

stack = deque()
# stack = []

# 스택 맨 끝에 데이터 추가
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
stack.append("E")

print(stack)  # 스택 출력

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
