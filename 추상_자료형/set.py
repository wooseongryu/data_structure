finished_classes = set()

# 데이터 저장
finished_classes.add("A")
finished_classes.add("B")
finished_classes.add("C")
finished_classes.add("D")
finished_classes.add("E")

print(finished_classes)  # 세트 출력

# 중복 데이터 저장 시도
finished_classes.add("A")  # 중복이 불가하다
finished_classes.add("B")

print(finished_classes)

# 데이터 탐색
print("A" in finished_classes)
print("B" in finished_classes)

# 데이터 삭제
finished_classes.remove("A")
finished_classes.remove("B")

print(finished_classes)
