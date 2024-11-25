SecretWord = str("chupacabra")
word = input("say the secret word : ")
while word != SecretWord:
    word = input("say the secret word : ")
    if word == str("chupacabra"):
        break
print("You've successfully left the loop.")