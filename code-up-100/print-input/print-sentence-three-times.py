# 문장을 입력받고 한줄에 세번 출력한다
sentence = input()

# solution 1
print(sentence, sentence, sentence)

# solution 2
for i in range(3):
    print(sentence, end=' ')

print()
# solution 3
print((sentence + ' ') * 3)

# solution 4
print(' '.join([sentence] * 3))

# solution 5
print(' '.join([sentence for i in range(3)]))

# solution 6
print(' '.join([sentence for _ in range(3)]))

