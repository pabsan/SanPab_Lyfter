from practice3 import list_sum

def test_sum_negative_number():
    #arrange
    my_list = [-2, -4, -6]
    #act
    result = list_sum(my_list)
    #assert
    assert result == -12


def test_sum_float_numbers():
    #arrange
    my_list = [3.1, 78.9, 2.33]
    #act
    result = list_sum(my_list)
    #assert
    assert result == 84.33


def test_sum_float_and_integers():
    #arrange
    my_list = [3.5, 2, 4.6, 6]
    #act
    result = list_sum(my_list)
    #assert
    assert result == 16.1