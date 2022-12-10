grades = {}

# key - value 데이터 삽입
grades["A"] = 80
grades["B"] = 90
grades["C"] = 70
grades["D"] = 85
grades["E"] = 95

print(grades)

# 한 key에 여러 value 저장 시도
grades["A"] = 100

print(grades)

# key를 이용해서 value 탐색
print(grades["A"])
print(grades["B"])

# key를 이용한 삭제
grades.pop("A")
grades.pop("B")

print(grades)
