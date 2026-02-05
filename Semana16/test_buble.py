from ejer1_buble import my_buble_sort
import random
import pytest

def test_bubble_small_list():
    #Arrange
    my_list = [5,3,8,6,2,3,7,4,1]
    #Act
    my_buble_sort(my_list)
    #Assert
    assert my_list == [1,2,3,3,4,5,6,7,8]


def test_bubble_long_list():
    #arrange
    my_list = []
    my_aux_list = []
    i =1
    for i in range(100):
        random_number = random.randint(1, 1000)
        my_list.append(random_number)
        my_aux_list.append(random_number)
    #act
    my_buble_sort(my_list)
    my_aux_list.sort()
    #assert
    assert my_list == my_aux_list


def test_bubble_empty_list():
    #arrange
    my_list = []
    #act
    my_buble_sort(my_list)
    #assert
    assert my_list == []


def test_bubble_element_is_not_list():
    #arrange
    my_list = "Esto no es una lista"
    #act & assert
    with pytest.raises(TypeError):
        my_buble_sort(my_list)

