from practice7 import primeNumbers

def test_prime_numbers_all_non_primes():
    #arrange
    my_list = [4, 6, 8, 9, 10]
    #act
    result = primeNumbers(my_list)
    #assert
    assert result == []


def test_prime_numbers_all_primes():
    #arrange
    my_list = [2, 3, 5, 7, 11]
    #act
    result = primeNumbers(my_list)
    #assert
    assert result == [2, 3, 5, 7, 11]


def test_prime_numbers_with_negative_and_zero():
    #arrange
    my_list = [-3, 0, 1, 2, 3]
    #act
    result = primeNumbers(my_list)
    #assert
    assert result == [2, 3]