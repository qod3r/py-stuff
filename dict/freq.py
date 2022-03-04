lines = int(input())

not_words = ["", " ", "\n", "\r", "\t"]
word_counter = dict()

for _ in range(lines):
    text = input().split(" ")

    for word in text:
        if word in not_words:
            continue
        
        if word not in word_counter:
            word_counter.update({word: 1})
        else:
            word_counter.update({word: word_counter[word] + 1})
            

sorted_counter = dict(sorted(word_counter.items(), key = lambda item: item[1], reverse = True))
print(sorted_counter)