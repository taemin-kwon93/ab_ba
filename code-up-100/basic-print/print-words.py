words = ["Hello", "World"]

def solution() -> str:
    some_context: str = ""
    for word in words:
        some_context += (word + " ")
        print(some_context)
    return some_context


greeting = solution()

print("출력결과 : " + greeting)
remove_space_end_of_greeting = greeting.strip()
print("공백제거 출력결과 : " + remove_space_end_of_greeting)