import unittest
from Lul import EmailValidator


class EmailValidatorTest(unittest.TestCase):
    def test_validate(self):
        validator = EmailValidator()
        self.assertEqual(validator.validater("work.cherepennikov@mail.ru"), "work.cherepennikov@mail.ru")
        self.assertEqual(validator.validater("work.cherepennikov@mai.l.ru"), None)
        self.assertEqual(validator.validater("овjob@rambler.com"), None)
        self.assertEqual(validator.validater("j@ob@rambler.com"), None)
        self.assertEqual(validator.validater("#job@rambler.com"), None)
        self.assertEqual(validator.validater("job.job@rambler.com"), "job.job@rambler.com")
        self.assertEqual(validator.validater(".jobjob@kk@mail.ru"), None)

if __name__ == '__main__':
    unittest.main()
