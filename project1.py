word = input("Enter a word: ")
char = input("Enter a character: ")
i = 0
count = 0
while i < len(word):
    if word[i] == char:
        count +=1
    i +=1

print(f"{char} has occured {count} times in {word}")