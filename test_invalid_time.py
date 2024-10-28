import pytest
from pytest import raises
from times import  time_range

def test_backward_time():
    with raises(ValueError, match="Time is backwards"):
        time_range("2010-01-13 10:00:00", "2010-01-12 12:00:00")

 