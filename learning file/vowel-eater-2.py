userWord = input("enter a word : ").upper()
wordWithoutVowels=""
for letter in userWord:
    if letter in ('A','E','I','O','U'):
        continue
    else:
        wordWithoutVowels += letter

print(wordWithoutVowels)