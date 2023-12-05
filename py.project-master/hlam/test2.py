from nltk import rewrite


def rewrite_article(title, text):
    # Заменяем все ссылки на статью на "здесь"
    title = rewrite(title, 'здесь')
    text = rewrite(text, 'здесь')

    # Заменяем все ссылки на статью на "в другом месте"
    title = rewrite(title, 'здесь')
    text = rewrite(text, 'в другом месте')

    # Заменяем все ссылки на статью на "в другом месте"
    title = rewrite(title, 'здесь')
    text = rewrite(text, 'в другом месте')

    return title, text


# Пример использования
original_title = "Моя статья"
original_text = "Это мой текст"

rewritten_title, rewritten_text = rewrite_article(original_title, original_text)
print("Заголовок:", rewritten_title)
print("Текст:", rewritten_text)