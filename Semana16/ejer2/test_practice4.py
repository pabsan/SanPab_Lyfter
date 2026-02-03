from practice4 import reverse_string

def test_string_palindrome():
    #arrange
    my_string = "madam"
    #act
    result = reverse_string(my_string)
    #assert
    assert result == "madam"


def test_string_with_numbers_and_characters():
    #arrange
    my_string = "123!abc"
    #act
    result = reverse_string(my_string)
    #assert
    assert result == "cba!321"


def test_empty_string():
    #arrange
    my_string = ""
    #act
    result = reverse_string(my_string)
    #assert
    assert result == ""