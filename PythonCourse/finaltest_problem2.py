__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 For this problem, you will write simple infinite generators for primes and fibonacci numbers.

 In addition you will write a simple generator common_elements function which returns the
 intersection of 2 given sorted iterators/iterables

'''

# Returns a generator which returns the sequence of primes infinitely.
# returns 2, 3, 5, 7, 11, 13,  ... successively
primes_list = []
def primes():
    primes_list.append(2)
    yield 2
    while True:
        n = next_prime()
        yield n
        primes_list.append(n)
    pass

def next_prime():
    num = primes_list[-1] + 1
    while True:
        if is_prime(num):
            return num
        num += 1

def is_prime(num):
    for d in primes_list:
        if num % d == 0:
            return False
    return True


# Returns a generator which returns the sequence of fibonacci numbers infinitely
# 1, 1, 2, 3, 5, 8, 13, ... successively (note that you should start from 1, 1 and not 0, 1)
def fibonacci_numbers():
    a = 1
    b = 1
    while True:
        yield a
        a += b
        a,b = b,a

    pass

# This is a generator which returns the common elements in both the first and second sorted iterators/iterables. If first
# and second are infinite, then this is also infinite. Assume that both first and second are sorted in ascending order.
# A simple use case for this is to find fibonacci numbers which are also primes using the two generators given above.
# It should work for any sorted iterator or iterable, so code accordingly.
#
# No special error checking required, allow errors to percolate up on wrong inputs.
def common_elements(seq1, seq2):
    prev_seq1 = None
    prev_seq2 = None
    seq1 = iter(seq1)
    seq2 = iter(seq2)
    prev_seq1 = seq1.next()
    prev_seq2 = seq2.next()

    while True:
        if prev_seq2 == prev_seq1:
            yield prev_seq1
            prev_seq1 = seq1.next()
            prev_seq2 = seq2.next()
        elif prev_seq1 < prev_seq2:
            prev_seq1 = seq1.next()
        else:
            prev_seq2 = seq2.next()


    pass


# write your own tests.
def test_primes():
    p = primes()
    pr = []
    for x in xrange(5):
        pr.append(p.next())
    assert pr == [2,3,5,7,11]
    pass


def test_fibonacci():
    f = fibonacci_numbers()
    fn = []
    for x in xrange(6):
        fn.append(f.next())
    assert fn == [1,1,2,3,5,8]
    pass

def test_common_elements():
    pass

