from contextlib import suppress
import phonenumbers


class EmailValidator:

    def validater(self, email):
        counter = 0
        kirill = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        find_kirill = [x for x in kirill if x in email.lower()]
        if len(find_kirill) > 0:
            return ""
        for letter in email:
            if letter == "@":
                counter += 1
        if counter > 1:
            return ""
        with suppress(Exception):
            [some_name, some_domen] = email.split("@")
            [some_domen, some_domen_zone] = some_domen.split(".")
        return some_name + "@" + some_domen + "." + some_domen_zone


class PhoneValidator:
    def validate(self, phone):
        normal = ""
        if phone[0] == '8':
            parse = phonenumbers.parse(phone, "RU")
            valid = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            parse = phonenumbers.parse(phone, "RU")
            valid = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.NATIONAL)
        for letter in valid:
            if letter.isalnum():
                normal += letter
        return normal


if __name__ == '__main__':
    Email = EmailValidator()
    Email1 = Email.validater("work.cherepennikov@mail.ru")
    print(Email1)
    Phone = PhoneValidator()
    Phone1 = Phone.validate("+79032225490")
    print(Phone1)
