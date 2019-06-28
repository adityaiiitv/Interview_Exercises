'''
Validation Test - Python

Created on Dec 6, 2016

@author: jpetrie

@description: This is the Validation Test in Python.
    This test should be fully self contained and capable of running on a fresh
    install (or virtual environment) of python.
        python val_py_test.py N
'''

# Validation Python Test #

##############
# Find Extra #
##############

# Given two arrays of unique strings, Small and Big.
# Big contains every element in Small, and has one additional unique member.
# For example:

Small = ['dog', 'cat', 'monkey']
Big = ['cat', 'rat', 'dog', 'monkey']

# Write a function to find the extra string in Big. #


def find_extra(smaller_one, bigger_one):
    val = list(set(bigger_one) - set(smaller_one))
    return val[0]

try:
    assert find_extra(Small, Big) == 'rat'
except AssertionError:
    print("Find Extra isn't working.")

###################
# Test Find Extra #
###################

# Write at least 6 fundamentally different test cases for find_extra
# Each test case should be a pair of arrays similar to Small and Big above
# Each test case should meet the requirements:
#    1. Arrays of unique elements
#    2. The Big array is a superset of the Small array, with one additional unique member
# Write out your test cases below in the same format as the one on line 24.

Small = ['@', '#', '$']
Big = ['@', '#', '$', '%']

Small = [1, 2, 3]
Big = [3, 2, 1, 0]

Small = [range(100)]
Big = [range(101)]

Small = ['dog', 'cat', 'monkey']
Big = ['cat', 'dog', 'monkey', 1]

Small = [1,2,3]
Big = [1,2,3,'dog']

Small = []
Big = [1]


###############
# Random Even #
###############

#  Write a program to output a random even number between 0 and N inclusive
#     using the random module and list comprehension.  Write your program such that
#     it can be run from a command line.  It should execute automatically when this file is run as in the description.

def random_even(N):
    import random
    val = 1
    while val%2!=0:
        val = random.randint(0,N)
    return val

####################
# Fibonacci Primes #
####################

# Calculate the largest prime value less than the nth value of the fibonacci sequence #
# The Fibonacci sequence is the series of numbers 0, 1, 1, 2, 3, 5, 8 ...
#     where the next number is found by adding the two numbers before it.  Xn = Xn-1 + Xn-2.
# The ratio of the top two numbers as the list grows approaches the golden ratio.
#     You can use this to find the nth fibonacci number.
# Xn = ((GOLDEN_RATIO^n) - (1 - GOLDEN_RATIO)^n)/sqrt(5)

# You can use this approximation for the golden ratio and the sqrt(5):
GOLDEN_RATIO = 1.618034  # Not exactly...
SQRT_FIVE = 2.236068  # Not exactly...

# The Sieve of Eratosthenes is one of the most efficient ways to find small primes.
# 1. Create a list of consecutive integers from 2 through n.
# 2. Let p equal 2 (the smallest prime)
# 3. Enumerate the multiples of p by counting to n from 2p in increments of p,
#     and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).
# 4. Find the first number greater than p in the list that is not marked. If there was no such number, stop.
#     Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
# - Wikipedia.

def fibo_prime(N):
    Xn = ((GOLDEN_RATIO**N) - (1 - GOLDEN_RATIO)**N)/SQRT_FIVE
    all_ints = list(range(2,int(round(Xn))))
    c1 = all_ints
    i = 0
    while i <len(all_ints):
        p = all_ints[i]
        j=i
        while j < len(c1):
            if all_ints[j]%p == 0 and i!=j:
                c1.remove(all_ints[j])
                j = j - 1
            j = j + 1
        all_ints = c1
        i = i + 1
    return all_ints[i-1]

try:
    assert fibo_prime(9) == 31
except AssertionError:
    print("Fibo Prime isn't working.")
    
if __name__ == "__main__":
    import sys
    print(__doc__)
    try:
        print("Received argument: %s" % sys.argv[1])
        print("Random Even %d" % random_even(int(sys.argv[1])))
        print("Fibo Prime: %d" % fibo_prime(int(sys.argv[1])))
    except (IndexError, TypeError):
        pass
