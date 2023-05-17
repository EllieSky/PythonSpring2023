import unittest
from parameterized import parameterized


def yodify_sentence(sentence: str):
    type_error_message = f'The argument passed to the function must be of type string. '\
                         f'Object passed to the function is of type "{str(type(sentence))[8:-2]}".'

    # throw error if argument passed is not a string
    if not isinstance(sentence, str):  # <- the way to check if a value is of type string
        raise TypeError(type_error_message)

    # detect the following (terminal) punctuation marks
    punctuation_chars = '?.!'

    # punctuation mark(s) at the end of the sentence
    ending = ''

    # flag for whether the sentence begins with a capital letter
    capitalized = sentence[0].isupper()

    # flag for whether the sentence begins with pronoun "I"
    # begins_with_cap_i = sentence[0:1] == "I "
    starts_with_cap_i = sentence.startswith("I ")

    # split the (stripped) sentence at white spaces, and store pieces in list
    words = sentence.split()

    # strip and store punctuation mark(s), if any, found at the end of the sentence
    while sentence[-1] in punctuation_chars:
        ending = sentence[-1] + ending
        sentence = sentence.removesuffix(sentence[-1])

    # unless the sentence begins with 'I ' then change the first word of the original sentence to lower case
    if not starts_with_cap_i:
        words[0] = words[0].lower()

    # if the original sentence begins with a capital letter then change its last word to upper case
    if capitalized:
        words[-1] = words[-1].capitalize()  # because it will become the first word of the "yodified" sentence

    # re-join pieces in the reverse order, and put punctuation back at the end
    yodified_sentence = ' '.join(words[::-1]) + ending
    return yodified_sentence


# original_sentence = input('Enter text or type "q" to quit: ')
# # original_sentence = "We are the champions!"
# if original_sentence != 'q':
#     print(f'Here is your sentence "yodified".\n{yodify_sentence(original_sentence)}')
# # yodify_sentence(original_sentence)


class YodifyFunctionTests(unittest.TestCase):

    @parameterized.expand([
        (
            'no caps no punctuation',
            'the rain in spain stays mainly in the plain',
            'plain the in mainly stays spain in rain the'
        ),
        (
            'caps first not I',
            'The rain in spain stays mainly in the plain',
            'Plain the in mainly stays spain in rain the'
        ),
        (
            'I first',
            'I wonder if the rain in spain stays mainly in the plain',
            'Plain the in mainly stays spain in rain the if wonder I'
        ),
        (
            'I first',
            'I wonder if the rain in Spain stays mainly in the plain',
            'Plain the in mainly stays Spain in rain the if wonder I'
        ),
        (
            'terminal punctuation single',
            'the rain in spain stays mainly in the plain.',
            'plain the in mainly stays spain in rain the.'
        ),
        (
            'terminal punctuation multiple',
            'the rain in spain stays mainly in the plain?!',
            'plain the in mainly stays spain in rain the?!'
        ),
        (
            'caps and terminal punctuation',
            'The rain in Spain stays mainly in the plain...',
            'Plain the in mainly stays Spain in rain the...'
        ),
        (
            'I first and terminal punctuation',
            'I wonder if the rain in Spain stays mainly in the plain...',
            'Plain the in mainly stays Spain in rain the if wonder I...'
        ),
        # TODO: support spaces trailing terminal punctuations
        #   (
        #       'terminal punctuation trailing space',
        #       'the rain in spain stays mainly in the plain?!  ',
        #       'plain the in mainly stays spain in rain the?!',
        #   )
        # TODO: support Proper names at the beginning of a sentence
        #   the only way to support this use case is likely to have a database of all proper nouns, names, etc.
        #     (
        #         'proper name first',
        #         'Alexey wonders if the rain in Spain stays mainly in the plain',
        #         'Plain the in mainly stays Spain in rain the if wonders Alexey'
        #     ),
        # TODO: support internal punctuation marks
        #     (
        #         'punctuation internal',
        #         'the snow, hail, and rain in Spain stay mainly in the plain; same in Bahrain',
        #         'Bahrain in same ;plain the in mainly stay Spain in rain and ,hail ,snow the'
        #     ),
        # TODO: support dashes, "dash-connected" words must be returned "connected-dash"
        #     (
        #         'dashes',
        #         'the rain-in-Spain stays mainly in the plain',
        #         'plain the in mainly stays Spain-in-rain the'
        #     ),
        # TODO: also support quotation marks, parentheses, and apostrophes
    ])
    def test_yodify_string(self, test_name, sentence, expected):
        actual = yodify_sentence(sentence)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        (
            'list',
            ['abc'],
            f'The argument passed to the function must be of type string. '
            f'Object passed to the function is of type "list".'
        ),
        (
            'dictionary',
            {'abc': '12', '34': 'ghj'},
            f'The argument passed to the function must be of type string. '
            f'Object passed to the function is of type "dict".'
        ),
    ])
    def test_yodify_nonstring(self, test_name, argument, expected_error):
        # self.assertRaises(TypeError, yodify_sentence, argument)
        self.assertRaisesRegex(TypeError, expected_error, yodify_sentence, argument)


if __name__ == '__main__':
    unittest.main()
