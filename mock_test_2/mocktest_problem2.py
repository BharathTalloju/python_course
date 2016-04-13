__author__ = 'Kalyan'

problem_notes = '''
This problem involves writing an iterator class that implements a CyclicCounter that take a value
and returns values descending down to 0 and then back to the value infinitely.

For e.g. for bound = 3. the iterator next() cycles through the values 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, ....

Notes:
- implement the methods of the class so that it behaves like an iterator with behavior described above
- a non positive value should raise ValueError
- no type checking required.
- you must use a constant amount of memory irrespective of the counter starting value (ie) I should be able to use
  really large values without running out of memory etc.
'''


class CyclicCounter(object):
    def __init__(self, high):
        self.high = high
        self.low = 0
        self.counter = high + 1
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
    pass


# a basic test is given, write your own tests.
def test_counter():
    c = CyclicCounter(2)
    # test the 1st 5 values, write
    i = 0
    result = []
    while i < 5:
        result.append(c.next())
        i += 1
    assert [2,1,0,1,2] == result
