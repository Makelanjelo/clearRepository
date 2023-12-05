from gensim.models import Word2Vec

text = "Я очень люблю свою маму"


# model = Word2Vec.load('data.bin')
words = text.split()
print(words)
rewritten_words = []
print(rewritten_words)
# for word in words:
#     synonyms = model.wv.synsets(word)
#     if synonyms:
#         rewritten_word = synonyms[0].name()
#         rewritten_words.append(rewritten_word)
#     else:
#         rewritten_words.append(word)
# rewritten_text = ' '.join(rewritten_words)
# print(rewritten_text)

