# Задача "Рассылка писем"
domain_control = ['.ru', '.net', '.com']


def domain_check_valid(email):
    for i in domain_control:
        if email[-len(i):] == i:
            domain_true = True
            if domain_true:
                return True
    return False


def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без @')
    if domain_check_valid(recipient) == False or domain_check_valid(sender) == False:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # if recipient.find('@') != -1 and sender.find('@') != -1:
    #     for i in domain_control:
    #         if recipient.find(i) != -1 and sender.find(i) != -1:
    #             return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    #         else:
    #             break
    # else:
    #     for i in domain_control:
    #         if not recipient.endswith(i):
    #             continue
    #         return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # if sender.find('@') == -1:
    #     for i in domain_control:
    #         if sender.find(i) == -1:
    #             domain_true_ = False
    #         else:
    #             domain_true_ = True
    #             if domain_true_:
    #                 break
    #             else:
    #                 print(f'Невозможно отправить письмо с адреса на адрес {recipient}')
    #     else:
    #         print(f'Невозможно отправить письмо с адреса на адрес {recipient}')
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