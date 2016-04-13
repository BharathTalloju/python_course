__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
Each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
For example, with a right shift of 3, A would be replaced by D, B would become E, and so on.
The method is named after Julius Caesar, who used it in his private correspondence.

Here is the complete capitals mapping for a shift of three:

Plain text  : ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher text : DEFGHIJKLMNOPQRSTUVWXYZABC

One more example:

Plaintext   : THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext  : WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ

The example shown above is a shift of three so that 
'B' in the plain-text becomes 'E' in the cipher-text,
'C' becomes 'F', the mapping wraps around so that 
'X' becomes 'A' and so on.

Your job is to write a set of routines that make it easy to encrypt a given text with this scheme.

- Write 3 routines as given below and test them independently.
- Read the comments carefully and satisfy the given constraints
- No type checking required unless explicitly asked for.
- Preserve the casing(lower case remains lower case, Uppercase remains upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.
'''
import string
# returns a dict which maps a letter to its corresponding final character
# you may use a dict comprehension with a helper nested function to create the cipher dict
# must map both lower case and upper case letters.
# no type checking required.
def make_cipher_map(k):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    c_lower_case = lower_case[k:] + lower_case[:k]
    c_upper_case = upper_case[k:] + upper_case[:k]
    e_map = dict(zip(lower_case, c_lower_case) + zip(upper_case, c_upper_case))
    return e_map
    pass

# Given a single word, return the cipher word of the same using the given cipher mapping
# Casing is preserved, non-letters are left as is in the final result.
# no type checking required.
def encrypt_word(word, cipher_map):
    cipher_word = ""
    for letter in word:
        if letter in cipher_map:
            cipher_word += cipher_map[letter]
        else:
            cipher_word += letter
    return cipher_word
    pass

# delegates to the above 2 helper methods to get the job done.
# raise TypeError is sentences is not a string or k is not an int
# k > 0  => right shift (A becomes B if K = 1)
# k < 0 =>  left shift (A becomes Z if K = -1)
# k = 0 => no encryption (A remains A)
def encrypt_text(sentence, k):
    if type(k) is not int:
        raise TypeError,"k is not int"
    if type(sentence) is not str:
        raise TypeError, "sentence is not string"

    cipher_map = make_cipher_map(k)
    words = sentence.split()
    cipher_text = []
    for word in words:
        cipher_text.append(encrypt_word(word, cipher_map))
    #print cipher_text
    cipher_text = " ".join(cipher_text)

    return cipher_text
    pass



def test_encrypt_text():
    assert "Ifmmp Xpsme!" == encrypt_text("Hello World!", 1)