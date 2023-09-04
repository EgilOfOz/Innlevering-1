alphabet_plain = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ., "
alphabet_encrypted = " abcdefghijklÆØÅmnopFGHIJKLMNOPQRSTUVWXYZqrstuvwxyzæøåABCDE.,"

sentence_plain = "Denne teksten skal bli kryptert."
sentence_encrypted = ""

for i in sentence_plain:
    num = 0
    for j in alphabet_plain:
        if i == j:
            sentence_encrypted = sentence_encrypted + alphabet_encrypted[num]
        num = num + 1 
print(sentence_encrypted)