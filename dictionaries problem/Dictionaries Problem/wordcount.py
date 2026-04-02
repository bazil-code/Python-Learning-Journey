sentence = "apple banana apple mango banana apple"
word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f'Word count: {word_count}')