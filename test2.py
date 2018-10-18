import unittest
from Lul import PhoneValidator


class PhoneValidatorTest(unittest.TestCase):
    def test_validate(self):
        validate = PhoneValidator()
        self.assertEqual(validate.validate("89032225490"), "+79032225490")
        self.assertEqual(validate.validate("+79032225490"), "+79032225490")
        self.assertEqual(validate.validate("+49032225490"), None)
        self.assertEqual(validate.validate("9032225490"), "+79032225490")
        self.assertEqual(validate.validate("8903р222549"), "+78903222549")


if __name__ == '__main__':
    unittest.main()