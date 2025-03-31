def analyse_text(text):
    # Приводим текст к нижнему регистру и разбиваем на слова
    words = text.lower().split()

    # Убираем знаки препинания из слов
    words = [''.join([char for char in word if char.isalnum()])
             for word in words]

    # Количество слов
    word_count = len(words)

    # Используем множество для подсчета уникальных слов
    unique_words = set(words)
    unique_words_count = len(unique_words)

    # Находим самое частое слово
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Преобразуем частоту в множество
    max_frequency = max(word_frequency.values())

    # Ищем слова с максимальной частотой
    most_common_words = {word for word,
                         freq in word_frequency.items() if freq == max_frequency}

    return word_count, unique_words_count, most_common_words, max_frequency
