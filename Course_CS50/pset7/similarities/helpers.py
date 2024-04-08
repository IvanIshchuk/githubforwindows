from nltk.tokenize import sent_tokenize

def lines(a, b):
    # Розділяємо рядки на список рядків, використовуючи символ нового рядка \n
    lines_a = a.splitlines()
    lines_b = b.splitlines()

    # Додаємо пустий рядок, якщо у вихідних рядках є пусті рядки
    clean_lines = [line.rstrip('\n') for line in set(lines_a) & set(lines_b)]
    empty_line_added = False

    if "" in lines_a or "" in lines_b:
        if not empty_line_added:
            clean_lines.append("")
            empty_line_added = True

    return clean_lines

def sentences(a, b):
    """Return sentences in both a and b"""

   # Розділяємо речення на список речень для обох вхідних рядків
    sentences_a = sent_tokenize(a)
    sentences_b = sent_tokenize(b)

    # Об'єднуємо унікальні речення з обох списків
    unique_sentences = set(sentences_a) & set(sentences_b)

    # Повертаємо список унікальних речень
    return list(unique_sentences)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # Створюємо множини для зберігання унікальних підрядків
    unique_substrings_a = set()
    unique_substrings_b = set()

    # Додаємо всі підрядки довжиною n з рядка 'a' у множину unique_substrings_a
    for i in range(len(a) - n + 1):
        unique_substrings_a.add(a[i:i+n])

    # Додаємо всі підрядки довжиною n з рядка 'b' у множину unique_substrings_b
    for i in range(len(b) - n + 1):
        unique_substrings_b.add(b[i:i+n])

    # Об'єднуємо множини унікальних підрядків
    unique_substrings = unique_substrings_a & unique_substrings_b

    # Повертаємо унікальні підрядки як список
    return list(unique_substrings)
