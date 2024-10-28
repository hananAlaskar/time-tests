import pytest
from times import compute_overlap_time, time_range


t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
t_2 = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00")

@pytest.mark.parametrize(
          "test_input1, test_input2,expected",
        [(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
           time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00"), [])]
        )
        
def test_time(test_input1, test_input2, expected):
    assert compute_overlap_time(test_input1, test_input2) == expected

# def test_no_overlap():
#     t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     t_2 = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00")
    
#     expected_no_overlap = []

#     assert compute_overlap_time(t_1, t_2) == expected_no_overlap



# def test_two_intervals():
#     t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
#     t_2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
#     expected_two_intervals = [("2010-01-12 10:30:00", '2010-01-12 10:37:00'),
#                                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

#     assert compute_overlap_time(t_1, t_2) == expected_two_intervals


# def test_adjacent_times():
#     t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     t_2 = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    
#     expected_adjacent_times = []
    
#     assert compute_overlap_time(t_1, t_2) == expected_adjacent_times


# def test_night():
#     t_1 = time_range("2010-01-12 10:00:00", "2010-01-13 02:00:00")
#     t_2 = time_range("2010-01-13 01:00:00", "2010-01-13 03:45:00")
    
#     expected_night_times = [("2010-01-13 01:00:00", "2010-01-13 02:00:00")]
    
#     assert compute_overlap_time(t_1, t_2) == expected_night_times