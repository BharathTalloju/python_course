__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    import string

    if type(base) is not int:
        raise TypeError
    if type(number) is not int:
        raise TypeError
    if base < 2 or base > 36:
        raise ValueError
    digits = list(string.digits) + list(string.ascii_uppercase)
    result = ''
    neg_flag = False

    if number < 0:
        number = -number
        neg_flag = True
    while number >= (base):
        r = number % base
        result = digits[r] + result
        number /= base
    result = digits[number] + result
    if neg_flag:
        result = '-' + result

    return result
    pass


def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print te