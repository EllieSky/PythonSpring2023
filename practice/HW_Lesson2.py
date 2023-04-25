import string
import unittest


def reverse_sentence(sentence :str):
    punctuation = ''
    capitalized = False

    if sentence[0].isupper():
        capitalized = True

    if sentence[-1] in '!?.;':
        punctuation = sentence[-1]
        sentence = sentence[:-1:]

    back_to_front = list(reversed(sentence.split()))
    if capitalized:
        back_to_front[0] = back_to_front[0].capitalize()

        if not back_to_front[-1] == 'I':
            back_to_front[-1] = back_to_front[-1].lower()

    result = ' '.join(back_to_front) + punctuation
    return result


class ReverseSentenceTestCase(unittest.TestCase):
    def test_reverse_basic_sentence(self):
        input = "monkeys are fun to watch at the zoo"
        expected = "zoo the at watch to fun are monkeys"
        self.assertEqual(expected, reverse_sentence(input))

    def test_reverse_capitalized_sentence(self):
        input = "Monkeys are fun to watch at the zoo"
        expected = "Zoo the at watch to fun are monkeys"
        self.assertEqual(expected, reverse_sentence(input))

    def test_reverse_sentence_with_punctuation(self):
        input = "Monkeys are fun to watch at the zoo!"
        expected = "Zoo the at watch to fun are monkeys!"

        self.assertEqual(expected, reverse_sentence(input))

    def test_reverse_sentence_with_I(self):
        input = "My friend and I think monkeys are fun to watch at the zoo."
        expected = "Zoo the at watch to fun are monkeys think I and friend my."
        self.assertEqual(expected, reverse_sentence(input))

    def test_reverse_sentence_that_starts_with_I(self):
        input = "I am awesome."
        expected = "Awesome am I."
        self.assertEqual(expected, reverse_sentence(input))

    def test_reverse_sentence_with_name_in_center(self):
        input = "The dog Steve was - blue;"
        expected = "Blue - was Steve dog the;"
        self.assertEqual(expected, reverse_sentence(input))

    @unittest.skip('broken')
    def test_reverse_sentence_with_multiple_punctuation(self):
        input = "He likes to run?! "
        expected = "Run to likes he?!"
        self.assertEqual(expected, reverse_sentence(input))


def palin(sentence :str):
    sentence = str(sentence).lower().replace(' ', '')
    filtered = ''
    for ch in sentence:
        if ch.isalnum():
            filtered += ch
    if filtered == filtered[::-1]:
        return True
    return False

print(palin(2002))
print(palin('kayak'))
print(palin('Hannah'))

print(palin('race car'))
print(palin('Was it a car or a cat I saw'))

print(palin('Do geese see God?'))
print(palin('Dammit, I’m mad!'))
print(palin('Oh, who was it I saw? Oh, who?'))


if __name__ == '__main__':
    unittest.main()
