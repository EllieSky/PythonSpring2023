import unittest


# 2002
# 2203
# ' '
# 'd'
# kayak
# Hannah
# race car
# Was it a car or a cat I saw
# Do geese see God?
# Dammit, I’m mad!
# Oh, who was it I saw? Oh, who?


def is_palin(data):
    data = str(data).lower()

    # Not needed anymore
    # data.replace(' ', '')

    clean_data = ''
    for ch in data:
        if ch.isalnum():
            clean_data += ch   # same as ->  clean_data = clean_data + ch

    if clean_data == clean_data[::-1]:
        return True
    return False


class IsPalindromeTests(unittest.TestCase):
    def test_using_int(self):
        input_int = 2002
        self.assertTrue(is_palin(input_int))

    def test_using_str(self):
        input_str = 'Hannah'
        self.assertTrue(is_palin(input_str))

    def test_using_non_polindrome(self):
        input_str = 'Watermelon'
        self.assertFalse(is_palin(input_str))

    def test_using_sentence(self):
        sentence = 'Oh, who was it I saw? Oh, who?'
        self.assertTrue(is_palin(sentence))

    def test_using_sentence2(self):
        sentence = 'Dammit, I’m mad!'
        self.assertTrue(is_palin(sentence))

if __name__ == '__main__':
    unittest.main()
