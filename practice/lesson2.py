import unittest

def count_chars(str, ch):
    new_case_str = str.lower()
    new_case_ch = ch.lower()
    return new_case_str.count(new_case_ch)
    # Optional: to do in one line
    # return str.lower().count(ch.lower())



class Lesson2(unittest.TestCase):
    def test_small_word(self):
        self.assertEqual(1, count_chars('word', 'w'))

    def test_mixed_case(self):
        self.assertEqual(2, count_chars('Cucumber', 'C'))

    def test_zero_count_chars(self):
        self.assertEqual(0, count_chars('Cucumber', 'z'))

    def test_bad_input(self):
        with self.assertRaises(AttributeError):
            count_chars('Cucumber', 4)

if __name__ == '__main__':
    unittest.main()
