import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("i like ", "burgers")
    assert result == "i like burgers"

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(10, 0)

# mark this test as slow, 
# execute marked tests: pytest -m slow
# execute all but marked: pytest -m "not slow"
@pytest.mark.slow
def test_divide_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2

# tests marked as skip are skipped
@pytest.mark.skip(reason="This feature is currently broken")
def test_add_bad():
    assert my_functions.add(1, 2) == 3

# this is "expected to fail"
@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4, 0)