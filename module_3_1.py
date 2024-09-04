# Задача "Счётчик вызовов"

calls = 0


def count_calls():
    global calls
    calls += 1 # Обновление значения в переменной calls с увеличением текущего на +1


def string_info(word):
    tuple_ = () # Создание пустого картежа
    for i in word:
        len_word = len(word) # Запись длины строки в отдельную переменную
        upper_word = word.upper() # Запись строки в верхнем регистре в отдельную переменную
        lower_word = word.lower() # Запись строки в нижнем регистре в отдельную переменную
        tuple_ = (len_word, upper_word, lower_word) # Добавление всех локальных переменных внутри функции в картеж tuple_
    count_calls() # Вызов функции count_calls
    return tuple_


def is_contains(word, list_words):
    match_found = False # Создание переменной в флагом
    for i in list_words: # Цикл перебора всех значений из списка list_word
        if word.lower() != i.lower(): # Преобразование строк из параметров word и list_words(i) в нижний регистр и их сравнение
            match_found = False # Если значение i не равно значению word, то значение в переменной match_found остается False
        else:
            match_found = True # Если значение i равно значению word, то значение в переменной match_found меняется на True
            break # Завершение выполнения цикла после нахождения совпадения
    count_calls() # Вызов функции count_calls
    return match_found # Функция возвращает значение переменной match_found


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
