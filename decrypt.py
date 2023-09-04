alphabet_plain = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ., "
alphabet_encrypted = " abcdefghijklÆØÅmnopFGHIJKLMNOPQRSTUVWXYZqrstuvwxyzæøåABCDE.,"

sentence_plain = ""
sentence_encrypted = "RdÆÆd.,pdjopdÆ,oj k,akh,jnJÅpdnpE"

for i in sentence_encrypted:
    num = 0
    for j in alphabet_encrypted:
        if i == j:
            sentence_plain = sentence_plain + alphabet_plain[num]
        num = num + 1 
print(sentence_plain)