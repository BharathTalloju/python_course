__author__ = 'Kalyan'

pytutor_technique = '''
This is useful when you are learning anything new. Using a visualizer to see if the code really does what you
think it does.

My suggestion for now is to ISOLATE A FAILING TEST (if you are running 10 inputs, which input fails?) and execute
the function in python tutor using those inputs and see what is going on.

Resources:
http://www.pythontutor.com/visualize.html#mode=edit
'''

# Fix this function so that it works as expected. See the tutor link at the bottom
# to debug this code in the tutor.
def buggy_reverse(input):
    input.reverse()
    return input


def test_buggy_reverse():
    assert [3,2,1] == buggy_reverse([1,2,3])
    assert [] == buggy_reverse([])
    input = ["a", "b", "c"]
    assert ["c", "b", "a"] == buggy_reverse(input)
    assert ["a", "b", "c"] == buggy_reverse(input)


# PY TUTOR LINK WITH CODE FOR ABOVE METHOD ALREADY SETUP
#
# http://pythontutor.com/visualize.html#code=def+buggy_reverse(input)%3A%0D%0A++++return+input.reverse()%0D%0A%0D%0Aassert+%5B3,2,1%5D+%3D%3D+buggy_reverse(%5B1,2,3%5D)&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0

# Copy paste the line above into your browser to see the function and assert already setup.
# Step through and see where the code fails. Feel free to edit the code in py tutor to investigate.



# Fix this code just like the above.
# you did for the problem above. http://pythontutor.com/visualize.html#mode=edit
def get_primes(count):
    result = []
    x = 2
    for x in range(2,50):
        c = 0
        j=2
        while j in range(x):
            if x % j == 0:
                c = c + 1
            j = j + 1

        if c == 0:
            result.append(x)
            if len(result) == count:
                 break

        if len(result) == count :
            break

    return result


# The code above has many bugs and many incorrect usages.
#   - infinite loop
#   - incorrect usage of loop conditions
#   - artificial bounds on x (50) based on the test cases input etc.
# Make sure you fix all of them.

def test_primes():
    assert [2] == get_primes(1)
    assert [2,3,5,7,11] == get_primes(5)
    assert [2,3,5,7,11,13,17,19,23,29] == get_primes(10)