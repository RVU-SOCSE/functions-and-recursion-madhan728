

text = input("Enter a sentence or paragraph: ")

words = text.lower().split()

word_count = {}

for word in words:
    
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        word_count[word] = word_count.get(word, 0) + 1


print("\nWord Count:")
for word, count in word_count.items():
    print(f"{word}: {count}")
