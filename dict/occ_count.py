text = input().split(" ")

not_words = ["", " ", "\n", "\r", "\t"]

word_counter = dict()

for word in text:
    if word in not_words:
        continue
    
    if word not in word_counter:
        word_counter.update({word: 1})
    else:
        word_counter.update({word: word_counter[word] + 1})
        
print(word_counter)