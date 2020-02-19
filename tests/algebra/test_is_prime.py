import pyrival.algebra


def test_is_prime():
    primes = set(pyrival.algebra.prime_list(100000))
    for i in range(100000):
        assert pyrival.algebra.is_prime(i) == (i in primes)

    assert pyrival.algebra.is_prime(10 ** 8 + 7) == True
    assert pyrival.algebra.is_prime(10 ** 9 + 7) == True
    assert pyrival.algebra.is_prime(10 ** 9 + 9) == True

    assert pyrival.algebra.is_prime(326549970232583195150330872691) == True
    assert pyrival.algebra.is_prime(551957180201435611622967802607) == True
    assert pyrival.algebra.is_prime(722963248890983103711213365897) == True

    assert pyrival.algebra.is_prime(688220523361999133670399137430) == False
    assert pyrival.algebra.is_prime(400284591585155461390239326086) == False
    assert pyrival.algebra.is_prime(576409959862662626347091665567) == False
