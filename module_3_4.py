# Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words = [] # Создание пустого списка
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower(): # Если слово из параметра root_word содержится в одном из слов списка other_word и наоборот,
            same_words.append(i) # то слово из списка other_word добавляется в список same_words
    return same_words # Функция возвращает список same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)