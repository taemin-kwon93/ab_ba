words = ["Hello", "World"]

def solution():
    sentence = ""
    for word in words:
        sentence += (word + " ")
        final_sentence = sentence.strip()
        # 반복문이 다 끝나면 print함수를 실행한다.
        if word == words[-1]:
            print("\"" + final_sentence + "\"")


solution()

