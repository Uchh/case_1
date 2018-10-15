import unittest
from Lul import PhoneValidator


class PhoneValidatorTest(unittest.TestCase):
    def test_validate(self):
        validate = PhoneValidator()
        self.assertEqual(validate.validate("89032225490"), "89032225490")
        self.assertEqual(validate.validate("+79032225490"), "89032225490")
        self.assertEqual(validate.validate("+49032225490"), "Error")
        self.assertEqual(validate.validate("9032225490"), "Error")


if __name__ == '__main__':
    unittest.main()