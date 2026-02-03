from practice6 import convert_to_list, sort_list

def test_convert_to_list_numbers_and_letters():
    #arrange
    my_string = "456-abc-123"
    #act
    result = convert_to_list(my_string)
    result = sort_list(result)
    #assert
    assert result == ["123", "456", "abc"]


def test_convert_to_list_mixed_case():
    #arrange
    my_string = "banana-Apple-grape-Orange"
    #act
    result = convert_to_list(my_string)
    result = sort_list(result)
    #assert
    assert result == ["Apple", "banana", "grape", "Orange"]


def test_convert_to_list_with_symbols():
    #arrange
    my_string = "hello-w*rld-pyt#on-rock$"
    #act
    result = convert_to_list(my_string)
    result = sort_list(result)
    #assert
    assert result == ["hello", "pyt#on", "rock$", "w*rld"]