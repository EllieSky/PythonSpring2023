import unittest
from parameterized import parameterized


def is_palindrome(candidate):
    type_error_message = f'The argument passed to the function must be of type string, integer, or float. '\
                         f'Object passed to the function is of type "{str(type(candidate))[8:-2]}".'

    # throw error if argument passed is not a string, an integer, or a float
    if not isinstance(candidate, (str, int, float)):  # <- check if a value is of type string, integer, or float
        raise TypeError(type_error_message)

    # handle float numbers ignoring the sign (negative float palindromes accepted)
    if isinstance(candidate, float):
        float_pieces = str(abs(candidate)).split('.')  # split into integral and fractional parts
        return float_pieces[0] == float_pieces[1][::-1]  # reverse of fractional part needs to be the same as integral

    # handle strings and integers
    candidate_alphanum = ''  # storage for string of only alphanumerical characters from the candidate
    for character in str(candidate).lower():  # cast candidate to lower case string and go through the string
        if character.isalnum():
            candidate_alphanum += character
    return candidate_alphanum == candidate_alphanum[::-1]


class PalindromeTests(unittest.TestCase):
    @parameterized.expand([
        ('word palindrome', 'kayak', True),
        ('word not palindrome', 'kayaks', False),
        ('word palindrome cap', 'Hannah', True),
        ('float palindrome', -123.321, True),
        ('float not palindrome', 123.21, False),
        ('int not palindrome', 2003, False),
        ('int palindrome', -40504, True),
        ('phrase palindrome', 'race car', True),
        ('phrase not palindrome', 'race cars', False),
        ('phrase palindrome cap', 'Race car', True),
        ('phrase palindrome punctuation1', 'Dammit, I’m mad!', True),
        ('phrase palindrome punctuation2', 'Oh, who was it I saw? Oh, who?', True),
    ])
    def test_palindrome(self, test_name, candidate, expected_verdict):
        self.assertEqual(is_palindrome(candidate), expected_verdict,)  # add assertion here

    @parameterized.expand([
        (
            'tuple',
            ('a', 'b', 2),
            f'The argument passed to the function must be of type string, integer, or float. '
            f'Object passed to the function is of type "tuple".'
        ),
        (
            'dictionary',
            {'abc': 12, '34': 'ghj', '56': 7.8},
            f'The argument passed to the function must be of type string, integer, or float. '
            f'Object passed to the function is of type "dict".'
        ),
    ])
    def test_palindrome_bad_input(self, test_name, argument, expected_error):
        # self.assertRaises(TypeError, is_palindrome, argument)
        self.assertRaisesRegex(TypeError, expected_error, is_palindrome, argument)


if __name__ == '__main__':
    unittest.main()
