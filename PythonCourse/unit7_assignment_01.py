__author__ = 'Kalyan'

profiling_timing = '''
This involves adding sufficient time.clock calls at appropriate places and then calculating difference to calculate
elapsed time.

http://docs.python.org/2/library/time.html?highlight=time.clock#time.clock

This is similar to print debugging, but once you have narrowed down code to a small code section by other means,
this can be very useful and precise.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit7_conversion_methods.py using time.clock() in this assignment.

for each value of count, execute the method 5 times and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

 Note: This is a python script which can be run from command line (python.exe <script>.py) or from pycharm (Right click -> Run <script>
 and not the usual pytest tests we have been using so far.
'''

import time
import unit7_conversion_methods

# write clean code to run all the profiles in one go using loops, lists etc. Note that functions are first class objects
# in python so you can hold them in a list.
def profile_clock():
    function_name = "numbers_string"

    for suffix in range(1,5):
        count = 10
        while(count != 1000000):
            actuals = []
            for x in xrange(5):
                f = getattr(unit7_conversion_methods, function_name+str(suffix))
                clock_before = (time.clock())
                f(count)
                clock_after = (time.clock())
                actuals.append(float(clock_after - clock_before))
            actuals.sort()
            print function_name+str(suffix)+",","count =",count, ", min =", actuals[0], ", actuals =", actuals
            count *= 10


    pass



# write your findings on what is the most optimal method and what you learnt in the process.
summary = '''


'''

if __name__ == "__main__":
    profile_clock()
