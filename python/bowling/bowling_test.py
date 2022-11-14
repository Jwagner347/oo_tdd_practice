import pytest

from bowling import Game, Frame

def test_can_parse_both_pins():
    frame = Frame("45")
    assert frame._first_pin == 4
    assert frame._second_pin == 5
    
def test_creates_correct_number_of_frames():
    frame_line = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert len(game._frames) == 10
    assert game.get_frame(1)._first_pin == 9
    assert game.get_frame(1)._second_pin == 0

def test_can_calculate_frame_score_ints_only():
    frame_line = '42|42|42|42|42|42|42|42|42|42||'
    game = Game(frame_line)
    
    assert game.get_frame(1)._frame_score == 6

def test_does_not_accept_score_greater_than_ten_per_frame():
    pass