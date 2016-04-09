__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Return the top n most frequently occurring chars and their respective counts
e.g aaaaaabbbbcccc, 2 should return [(a 5) (b 4)]
in case of a tie, return char which comes earlier in alphabet ordering
e.g. cdbba,2 -> [(b,2) (a,1)]
use standard types and and builtin functions we have used in the course.

constraints:
1. raise TypeError if word is not a str or n is not an int
2. raise ValueError if n <= 0,
3. if n > number of unique chars just return the available chars and their counts
2. The function should be case sensitive (ie) A and a are different. So aaAABBB, 2 should return [(B,3), (A,2)]
'''
import collections

def top_chars(word, n):
    if type(word) is not str:
        raise TypeError, "Only string allowed as the first argument"
    if type(n) is not int:
        raise TypeError, "only int allowed as second argument"
    if n<= 0:
        raise ValueError,"Second argument must be greater than 0"

    no_of_unique_letters = len(set(word))

    count_of_chars = collections.defaultdict(int)
    for char in word:
        count_of_chars[char] += 1

    if no_of_unique_letters < n:
        return [(x,count_of_chars[x]) for x in count_of_chars]

    result = [(x,count_of_chars[x]) for x in count_of_chars]
    result.sort(key = lambda e: (e[1], -ord(e[0])), reverse = True)

    return result[:n]

    pass


#write your own tests.
def test_top_chars():
    assert [('a',5),('b',4)] == top_chars("aaaaabbbbcccdde", 2)
    assert top_chars("aaAABBB",2) == [('B',3),('A',2)]