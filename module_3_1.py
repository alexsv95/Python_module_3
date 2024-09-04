# Задача "Счётчик вызовов"

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(word):
    tuple_ = ()
    for i in word:
        len_word = len(word)
        upper_word = word.upper()
        lower_word = word.lower()
        tuple_ = (len_word, upper_word, lower_word)
    count_calls()
    return tuple_


def is_contains(word, list_words):
    match_found = True
    for i in list_words:
        if word.lower() != i.lower():
            match_found = False
        else:
            match_found = True
            break
    count_calls()
    return match_found


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
