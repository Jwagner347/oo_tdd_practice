import pytest

from bowling import Frame

def test_can_calculate_total_pins():
    ten_pin_frame = Frame("45")
    assert ten_pin_frame.calculate_frame_score() == 9

