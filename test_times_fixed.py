import pytest
from times import time_range, compute_overlap_time_fixed


def test_no_overlap_for_fixed():
    t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    t_2 = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00")
    
    expected_no_overlap = []

    assert compute_overlap_time_fixed(t_1, t_2) == expected_no_overlap



def test_two_intervals_for_fixed():
    t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    t_2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    expected_two_intervals = [("2010-01-12 10:30:00", '2010-01-12 10:37:00'),
                               ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert compute_overlap_time_fixed(t_1, t_2) == expected_two_intervals


def test_adjacent_times_for_fixed():
    t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    t_2 = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    
    expected_adjacent_times = []
    
    assert compute_overlap_time_fixed(t_1, t_2) == expected_adjacent_times