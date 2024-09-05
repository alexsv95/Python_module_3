# Задача "Рассылка писем"

def email_valid(email):
    if not '@' in email:
        return False

    domain_control = ['.ru', '.net', '.com']
    for i in domain_control:
        if email[-len(i):] == i:
            return True
    return False


def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if email_valid(recipient) == False or email_valid(sender) == False:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient == sender:
        return print('Нельзя отправить письмо самому себе!')
    if sender == 'university.help@gmail.com':
         return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')