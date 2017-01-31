# Highly divisible triangular number
#
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

import sys;

def get_factor_count(n):
    global primes;
    global prime_count;
    global prime_max;
    global sieve;
    factor_count = 1;
    prime_index = 0;
    prime = primes[prime_index];
    while n > 1:
        # If n is prime, there are exactly 2 * the curent factor_count. Exit the outer loop.
        if n <= prime_max and sieve[n]:
            factor_count *= 2;
            break;
        prime = primes[prime_index];
        current_prime_factor_count = 0;
        while n % prime == 0:
            current_prime_factor_count += 1;
            n /= prime;
        factor_count *= (current_prime_factor_count + 1);
        prime_index += 1;
        if prime_index >= prime_count:
            print "get_factor_count(%d) failed due to insufficiently large primes table." % n;
            sys.exit();
    return factor_count;

# Read the primes from a file, and initialize the Sieve of Eratosthenes.
primes = [];
infile = open("primes_below_2_million.txt", "r");
for line in infile:
    primes.append(int(line));
infile.close();
prime_count = len(primes);
prime_max = primes[-1];
print "known prime count = %d" % prime_count;
print "known prime max   = %d" % prime_max;
sieve = [False] * (prime_max + 1);
for prime in primes:
    sieve[prime] = True;

D = 500;
n = 0;
i = 0;
while True:
    i += 1;
    n += i;
    d = get_factor_count(n);
    print "%d: %d has %d divisors" % (i, n, d);
    if d > D:
        break;

