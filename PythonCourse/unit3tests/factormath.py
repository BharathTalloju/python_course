"""Contains functions for Unit_3 assignments"""
import collections

primes_list = []

def factorize_number(number):
    if type(number) != int and type(number) != long:
        raise TypeError
    if type(number) == long:
        number = int(number)
    if number < 0 :
        raise ValueError
    marker = 1
    d = collections.defaultdict(int)
    if number == 1:
        return []
    #if is_prime(number):
        return [(number,1)]

    while number != 1:
        next_prime(marker)
        for x in primes_list:
            if number % x == 0:
                d[x] += 1
                number = number / x
        marker = primes_list[-1]
    result = []
    for r in d:
        result.append((r,d[r]))
    result.sort(key = lambda f: f[0])
    return result





def is_prime(i):
    for x in primes_list:
        if (i%x) == 0:
            return False
    return True


def next_prime(number):
    "Returns the immediate prime number after number"

    if number == 1:
        primes_list.append(2)
        return 2
    if is_prime(number+1):
        primes_list.append(number+1)
        return number + 1
    return next_prime(number+1)


def get_hcf(first, second):
    min_power = lambda x,y: min((x,y),key = lambda x: x[1])
    common = []
    #dict_first = dict(first)
    dict_second = dict(second)
    for f in first:
        if f[0] in dict_second:
            common += min_power(f,(f[0],  dict_second[f[0]]))
    result = zip(common[::2],common[1::2])
    return result

def get_lcm(first,second):
    result = collections.defaultdict(int)
    for f in first:
        if result[f[0]] < f[1]:
            result[f[0]] = f[1]
    for s in second:
        if result[s[0]] < s[1]:
            result[s[0]] = s[1]
    lcm = []
    for r in result:
        lcm.append((r,result[r]))
    lcm.sort()
    return lcm

def multiply(first,second):
    result = collections.defaultdict(int)
    for f in first:
        result[f[0]] = f[1]
    for s in second:
        result[s[0]] += s[1]
    product = []
    for r in result:
        product.append((r,result[r]))
    product.sort()
    return product