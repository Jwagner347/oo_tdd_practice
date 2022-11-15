import pytest

from bowling import Game, Frame

def test_can_parse_both_pins():
    frame = Frame("45")
    assert frame._first_ball == "4"
    assert frame._second_ball == "5"
    
def test_creates_correct_number_of_frames():
    frame_line = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert len(game._frames) == 10
    assert game.get_frame(1)._first_ball == "9"
    assert game.get_frame(1)._second_ball == "-"

def test_can_calculate_frame_score_ints_only():
    frame_line = '42|42|42|42|42|42|42|42|42|42||'
    game = Game(frame_line)
    
    assert game.get_frame(1)._frame_score == 6
    
def test_can_calculate_frame_score_with_no_ball():
    frame_line = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert game.get_frame(1)._frame_score == 9
    
def test_can_calculate_frame_score_with_spares():
    frame_line = '9-|5/|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert game.get_frame(2)._frame_score == 10
    
def test_can_calculate_frame_score_with_strikes():
    frame_line = '9-|X|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert game.get_frame(2)._frame_score == 10
    
def test_can_handle_bonus_balls_at_end():
    frame_line = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5'
    game = Game(frame_line)
    
    assert game.get_frame(11)._frame_score == 5
    
# def test_can_handle_no_bonus_balls_at_end():
#     frame_line = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5-||'
#     game = Game(frame_line)
    
#     assert game.get_frame(11)._frame_score == 5

def test_does_not_accept_score_greater_than_ten_per_frame():
    pass