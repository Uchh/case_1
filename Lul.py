from contextlib import suppress
from Logo import Logo
import phonenumbers


class EmailValidator:

    #
    #       Соответсвует правилам почт сервиса mail.ru
    #
    def validater(self, email):
        counter = 0
        legit_letters = ('qazwsxedcrfvtgbyhnujmiklop1234567890_.-')
        kirill = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        find_wrong = [x for x in legit_letters if x in email.lower()]
        if len(find_wrong) == 0:
            return None
        find_kirill = [x for x in kirill if x in email.lower()]
        if len(find_kirill) > 0:
            return None
        if email[0].isalnum():
            for letter in email:
                if letter == "@":
                    counter += 1
            if counter > 1:
                return None
            with suppress(Exception):
                [some_name, some_domen] = email.split("@")
                [some_domen, some_domen_zone] = some_domen.split(".")
                return some_name + "@" + some_domen + "." + some_domen_zone
        else:
            return None

    #
    #       Уберает все буквы и лишние символы, нормализует телефоны под интернациональный вид с кодом +7
    #       Внимание! Такой номер как 8903р222549 не выдаст ошибку, переделается в +78893222549,
    #       что в целом не является ошибкой!

class PhoneValidator:
    def validate(self, phone):
        correct_phone = ""
        normal = ""
        for letter in phone:
            if letter.isnumeric() or letter == '+':
                correct_phone += letter
        for letter in correct_phone:
            if len(correct_phone) == 10:
                with suppress(Exception):
                    parse = phonenumbers.parse(correct_phone, "RU")
                    valid = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            elif len(correct_phone) == 11:
                if correct_phone[0] == '8':
                    with suppress(Exception):
                        parse = phonenumbers.parse(correct_phone, "RU")
                        valid = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            elif len(correct_phone) == 12:
                if correct_phone[0] == '+' and correct_phone[1] == '7':
                    with suppress(Exception):
                        parse = phonenumbers.parse(correct_phone, "RU")
                        valid = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        with suppress(Exception):
            for letter in valid:
                if letter.isnumeric() or letter == '+':
                    normal += letter
            return normal


if __name__ == '__main__':
    Email = EmailValidator()
    Email1 = Email.validater("karasev_marker357@gmail.com")
    print(Email1)
    Phone = PhoneValidator()
    Phone1 = Phone.validate("8-927-001-42-78")
    print(Phone1)
    logo = Logo()
    otrisovka = logo.otrisovka()
