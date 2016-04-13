__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''
import string

def smallest_palindrome(word):
    if type(word) is not str:
        raise TypeError,"Not a string parameter"
    valid_chars = set(string.ascii_letters)
    word_chars = set(word)
    if word_chars - valid_chars != set():
        raise ValueError, "Only alphabets allowed"

    word = word.strip()
    if is_palindrome(word):
        return word
    suffix = ''
    for i in xrange(len(word)):
        if not is_palindrome(word[i:]):
            suffix += word[i].lower()
        else:
            break
    word += suffix[-1::-1]
    return word

    pass

def is_palindrome(word):
    if word == '':
        return True
    length = len(word) - 1
    word = word.lower()
    for i in xrange(length+1/ 2):
        if word[i] != word[length - i]:
            #print word[i], '!=', word[length - i]
            return False
    #print word,'is palindrome'
    return True

# write your own tests
def test_smallest_palindrome():
    assert  'Malayalam' == smallest_palindrome('Malayalam')
    assert 'Malayalam' == smallest_palindrome('Malayal')
    assert 'Madam' == smallest_palindrome('Mad')
    assert 'aaa' ==smallest_palindrome('aaa')
    assert 'mxcxm'==smallest_palindrome('mxc')
    pass


