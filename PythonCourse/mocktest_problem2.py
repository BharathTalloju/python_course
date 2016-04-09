__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 This problem deals with number conversion from a custom base 26 notation.

 In this notation, the letters a to z are used for digits 0 to 25. E.g.
 decimal 10 in this notation will be "k" and 26 will be "ba" The notation in
 case insensitive so even Ba is a valid representation for 26.

 Your job is to write a decoding routine for this notation.

 Note: make good use of python features and avoid huge if else statement flow!
'''

import string

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int or long that corresponds to the number.
def from_custom_base26(s):
    if type(s) is not str:
        raise TypeError, "from_custom_base26() takes only one string argument"

    if len(s) == 0:
        raise ValueError, "Empty string cannot be decoded"

    s = s.lower()
    legal_characters = list(string.ascii_lowercase + '-' + '+')
    legal_character_set = set(legal_characters)
    if (set(s)-legal_character_set) != set():
        raise ValueError, "Encoding is not right"

    negative = False
    if '-' in set(s):
        negative = True

    s = s.replace('-','')
    s = s.replace("+",'')
    s = s[::-1]
    values = range(26)
    mapping = dict(zip(legal_characters, values))

    multiplier = 1
    result = 0

    for letter in s:
        if letter not in legal_character_set - set('-+'):
            ValueError, "Encoding is not correct"
        result += mapping[letter]*multiplier
        multiplier *= 26

    if negative:
        result = -result

    return result




# a basic test is given, write your own tests based on constraints.
def test_from_custom_base26():
    assert 29 == from_custom_base26("bd")