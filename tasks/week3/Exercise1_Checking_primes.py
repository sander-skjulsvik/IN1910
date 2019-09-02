
def is_prime(n):
    # print(f'n = {n}')
    '''
        Returns a boolean value, True if prime or false if not a prime.
        1st check right input, 2nd check if 
    '''
    #1st
    if not (isinstance(n, int) and n > 0):
        raise TypeError(f"input must be a int and bigger than 0, n = {n}, type(n) = {type(n)}")
    #2nd
    if n == 3 or n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i < n:
            # print(f'i = {i}')
            if n % i == 0:
                return False
            i += 2
    #3rd
    return True


def test_is_prime():
    primes = [19, 7919, 5209]
    numbers = [200, 25, 12345]
    non_numbers = [lambda x: x*2, [1,2,3,], {1:2,'hello, world':'!'}, '2']
    for i in primes:
        assert is_prime(i), 'primes'
    for i in numbers:
        msg =  f'not primes, n = {i}'
        assert not is_prime(i), msg
    for i in non_numbers:
        pass

if __name__ == "__main__":
    test_is_prime()
