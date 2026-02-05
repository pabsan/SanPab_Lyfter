from practice5 import string_count

def test_string_mixed_case():
    #arrange
    my_string = "Hello World"
    #act
    result = string_count(my_string)
    #assert
    assert result == "There's 2 upper cases and 8 lower cases"


def test_string_all_lowercase():
    #arrange
    my_string = "this is a test"
    #act
    result = string_count(my_string)
    #assert
    assert result == "There's 0 upper cases and 11 lower cases"


def test_string_with_numbers_letters_and_symbols():
    #arrange
    my_string = "1234!@#$aQ"
    #act
    result = string_count(my_string)
    #assert
    assert result == "There's 1 upper cases and 1 lower cases"