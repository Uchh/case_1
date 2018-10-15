from contextlib import suppress
import phonenumbers


class EmailValidator:

    def validater(self, email):
        counter = 0
        kirill = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        find_kirill = [x for x in kirill if x in email.lower()]
        if len(find_kirill) > 0:
            return "Error"
        for letter in email:
            if letter == "@":
                counter += 1
        if counter > 1:
            return "Error"
        with suppress(Exception):
            [some_name, some_domen] = email.split("@")
            [some_domen, some_domen_zone] = some_domen.split(".")
            return some_name + "@" + some_domen + "." + some_domen_zone


class PhoneValidator:
    def validate(self, phone):
        correct_phone = ""
        normal = ""
        for letter in phone:
            if letter.isnumeric() or letter == '+':
                correct_phone += letter
            else:
                return "Error"
        if correct_phone[0] == '8':
            parse = phonenumbers.parse(correct_phone, "RU")
            valid = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.NATIONAL)
        elif correct_phone[0] == '+' and correct_phone[1] == '7':
            parse = phonenumbers.parse(correct_phone, "RU")
            valid = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            return "Error"
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
