__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Pig latin is an amusing game to conceal the meaning of a sentence.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants before the first vowel to the end and add  "ay" at the end.
e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

Your job is to write a routine that will convert a given text to pig latin. e.g "There is, however, no need for fear."
should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."  Note that punctuation and
capitalization has to be preserved

You can write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and
will be followed by a space if there is a next word. Acronyms are not allowed in sentences.
Some words may be capitalized (first letter is capital like "There" in the above example)
and you have to preserve its capitalization in the final word too (Erethay)

You can assume that only valid inputs as specified above will be given.
'''
import string
def get_pig_latin(sentence):
    Capital_letters = string.ascii_uppercase
    consonants = set(string.ascii_letters) - set("aeiouAEIOU")
    vowels = set("aeiouAEIOU")
    words = sentence.split(' ')
    first_occurances_of_vowel = [find_first_occurances_of_vowel(word) for word in words]

    is_capitalized = [(x[0] in Capital_letters) for x in words]
    words = [word.lower() for word in words]

    for word,first_occurances_of_v in words,first_occurances_of_vowel:


    pass

def find_first_occurances_of_vowel(word):
    vowels = set("aeiouAEIOU")
    index = 0
    for x in range(len(word)):
        if word[x] in vowels:
            return x


# write your own tests according to the constraints and notes given above.
def test_get_pig_latin():
        assert "onay earfay" == get_pig_latin("no fear")



