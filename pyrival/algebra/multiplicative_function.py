# Computes f(x) for x = 1,...,n in O(n log log n) time, 
# where f is a multiplicative function.
# Input:
#  function g: g(p,k) = f(p**k) where p is prime and k>0
#  n: How many values to compute
#  u: Used as uninitialized value. Can be anything expect
#     that u != f(x) for x = 1,..,n.
 
def compute_multiplicative_function(g, n, u=-2):
    DP = [u] * (n + 1)
    DP[1] = 1
    for p in range(2, n + 1):
        if DP[p] == u: # if p prime
            k = 1
            upper = n // p 
            while upper: # Overflow-safe check for n // p**k > 0
                pk = p**k
                f_pk = g(p, k)
                for j in range(1, upper + 1):
                    DP[j*pk] = DP[j] * f_pk
                k += 1
                upper //= p
    return DP


# Examples

n = 20

# Euler's totient function
# i.e. count of numbers < x that are relative prime to x
totient_g = lambda p,k: p**(k - 1) * (p - 1)
totient = compute_multiplicative_function(totient_g, n)

# The Mobius function
# Useful for inclusion-exclusion
mobius_g = lambda p,k: -1 if k==1 else 0
mobius = compute_multiplicative_function(mobius_g, n)

# Count number of divisors of x (including 1 and x)
divcount_g = lambda p,k: k + 1
divcount = compute_multiplicative_function(divcount_g, n)
# Is prime iff divisor count == 2
primes = [i for i in range(n + 1) if divcount[i] == 2]

# Compute sum of all divisors of x
divsum_g = lambda p,k: (p**(k + 1) - 1) // (p - 1)
divsum = compute_multiplicative_function(divsum_g, n)
