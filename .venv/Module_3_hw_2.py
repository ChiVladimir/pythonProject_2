def validity_address(email):

    check = ['.com', '.net', '.ru']
    i = len(email)
    ctrl = str(email[-3:i])
    if '.' not in ctrl:
        ctrl = str(email[-4:i])
    res = ctrl in check
    if '@' not in email:
        res = False
    return res


def send_email(message, recipient, sender = "university.help@gmail.com"):

    recipient_check = validity_address(recipient)
    sender_check = validity_address(sender)

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif recipient_check == False or sender_check == False:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient_check == True and sender_check == True and sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    elif recipient_check == True and sender_check == True and sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')