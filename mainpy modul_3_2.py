def send_email(message, recipient, *, sender="university.help@gmail.com"):
    """
    Функция для отправки электронных писем.

    :param message: Текст сообщения
    :param recipient: Адрес получателя
    :param sender: Адрес отправителя (по умолчанию university.help@gmail.com)
    """

    # Функция для проверки корректности email адреса
    def is_valid_email(email):
        return "@" in email and email.endswith((".com", ".ru", ".net"))

    # Проверка корректности email адресов
    if not (is_valid_email(sender) and is_valid_email(recipient)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на стандартного отправителя
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


# Тестовые вызовы функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')