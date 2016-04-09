__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 This is another custom encryption scheme that was in popular use to send secret messages in olden days. In this
 scheme successive letters are written in different lines by hand and all the characters are merged line by line
 to create the final encrypted text. The number of lines can differ and is an input to this problem.

 Write encode and decode routines for this cipher given a text and the number of lines n.

 E.g "Hello Cat" with line count 2 when written over 2 lines is:
line1:              H   l   o    C   t
line2:                e   l   ' '  a

    So final text is "HloCtel a" (characters of line 1 followed by characters of line2)

Similarly a word "Popular" with line count 3 will be
line1:            P       l
line2:              o   u   a
line3:                p       r

    So final text is Plouapr

Constraints and notes:
1. Write the cipher routines work for arbitrary n. Raise value error if n <= 0
2. Assume types are correct
3. Note that the encryption is not done word by word but for the whole text at one go. See the "Hello cat" example, the
   space was treated as part of text and it moved.
4. Make good use of python builtins and data structures. Note that successive characters will go into lines
   1, 2, 3, 2, 1, 2, 3, 2, 1, ... for n=3 (repeating pattern)
5. Note that you are writing a program to solve this, so you can just use plain code and additional data structures
   to solve this instead of finding mathematical patterns (that is also allowed :-) ).
'''

def encode(text, n):
    c = CyclicCounter(n)
    lines = []
    for i in xrange(n):
        lines.append('')

    n -= 1
    for letter in text:
        line = c.next() - 1
        print line
        lines[line] += letter
    c_text = ''
    for line in lines:
        c_text += line
    return c_text
    pass

def decode(text, n):
    p_text = ''
    c = CyclicCounter(n)
    reader = -1
    l = len(text)
    for i in xrange(len(text)):
        n = c.next()
        reader += n
        if reader > l:
            reader = reader - 2*n
        reader = reader % l
        p_text += text[reader]

    return p_text
    pass


class CyclicCounter(object):
    def __init__(self, high):
        self.high = high
        self.low = 1
        self.counter = self.low -1
        self.increment = -1

    def __iter__(self):
        return self

    def next(self):
        if self.counter >= self.high:
            #print self.counter,">=",self.high
            self.increment = -1
        elif self.counter <= self.low:
            self.increment = 1
        self.counter += self.increment
        #print "returning ", self.counter
        return self.counter
# write your own tests.
def test_encode():
    pass

def test_decode():
    pass
