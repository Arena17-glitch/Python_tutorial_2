sentence = "Python is great and Python is easy"
sentence = sentence.lower()
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
