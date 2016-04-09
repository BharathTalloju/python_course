__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, preserve the original order.

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.

Note: use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
'''
import string

def transform(sentence):

    if type(sentence) != str:
        raise TypeError, "transform takes only one argument, a string"

    legal_characters = set(string.ascii_letters + ' ')
    input_characters = set(sentence)

    if (input_characters - legal_characters) != set():
        raise ValueError, "Only a-z,A-Z allowed"

    words_list = sentence.split()

    words_list.sort(key = lambda e: (-len(e), count_vowels(e)))

    return " ".join(words_list)

    pass

def count_vowels(word):
    count = 0
    word = word.lower()
    vowels = set(['a','e','i','o','u'])
    for letter in word:
        if letter in vowels:
            count += 1

    return count


def test_transform():
    assert "elephant walking runway down seen was the An" == transform("An elephant was seen walking down the runway")