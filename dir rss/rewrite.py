from gensim.summarization import summarize

# Исходный текст
text = "Передо мной сидит самая прекрасная девушка на свете, какой комплимент мне ей сказать?"

# Суммирование текста
summary = summarize(text)

# Рерайт текста
rewritten_text = gensim.utils.simple_preprocess(summary)

# Вывод рерайта
print(rewritten_text)

